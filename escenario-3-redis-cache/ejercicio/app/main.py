from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
import redis
import psycopg2
import json
import os

app = FastAPI(title="API FastAPI + Redis + PostgreSQL")

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    decode_responses=True
)


def obtener_conexion():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "db"),
        port=int(os.getenv("DB_PORT", 5432)),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", "postgres"),
        database=os.getenv("DB_NAME", "apidb")
    )


@app.middleware("http")
async def rate_limit(request: Request, call_next):
    ip = request.client.host
    clave = f"rate_limit:{ip}"

    cantidad = redis_client.get(clave)

    if cantidad is None:
        redis_client.setex(clave, 60, 1)
    else:
        cantidad = int(cantidad)

        if cantidad >= 10:
            return JSONResponse(
                status_code=429,
                content={
                    "detail": "Limite de 10 solicitudes por minuto excedido"
                }
            )

        redis_client.incr(clave)

    response = await call_next(request)
    return response


@app.get("/")
def inicio():
    return {
        "servicio": "FastAPI con Redis y PostgreSQL",
        "status": "activo"
    }


@app.get("/health")
def health():
    try:
        redis_client.ping()

        conexion = obtener_conexion()
        conexion.close()

        return {
            "status": "healthy",
            "redis": "OK",
            "postgresql": "OK"
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        )


@app.get("/contador")
def contador():
    visitas = redis_client.incr("contador_visitas")

    return {
        "visitas": visitas
    }


@app.get("/usuarios")
def obtener_usuarios():
    cache_key = "usuarios_cache"

    datos_cache = redis_client.get(cache_key)

    if datos_cache:
        return {
            "origen": "cache",
            "usuarios": json.loads(datos_cache)
        }

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute(
        "SELECT id, nombre, email FROM usuarios ORDER BY id"
    )

    filas = cursor.fetchall()

    cursor.close()
    conexion.close()

    usuarios = [
        {
            "id": fila[0],
            "nombre": fila[1],
            "email": fila[2]
        }
        for fila in filas
    ]

    redis_client.setex(
        cache_key,
        60,
        json.dumps(usuarios)
    )

    return {
        "origen": "postgresql",
        "usuarios": usuarios
    }


@app.delete("/cache")
def limpiar_cache():
    redis_client.delete("usuarios_cache")

    return {
        "mensaje": "Cache eliminada"
    }