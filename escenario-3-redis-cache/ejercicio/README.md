# Escenario 3: FastAPI + Redis + PostgreSQL

Este escenario implementa una API desarrollada con FastAPI que utiliza PostgreSQL como fuente principal de datos y Redis como sistema de caché.

La aplicación se ejecuta mediante Docker Compose y cuenta con persistencia de datos, healthchecks, rate limiting y separación entre configuración de desarrollo y producción.

## Servicios

La solución está compuesta por tres servicios:

FastAPI:
Aplicación principal disponible en el puerto 8000.

Redis:
Utilizado para caché, contador de visitas y rate limiting.

PostgreSQL:
Utilizado como fuente principal de datos.

## Estructura

escenario-3-redis-cache/ejercicio/

docker-compose.yml

docker-compose.override.yml

app/
    Dockerfile
    requirements.txt
    main.py

db/
    init.sql

## Levantar el entorno de desarrollo

Ubicarse en:

escenario-3-redis-cache/ejercicio

Ejecutar:

docker-compose up --build -d

Docker Compose utiliza automáticamente:

docker-compose.yml

y:

docker-compose.override.yml

El archivo override monta el código fuente dentro del contenedor y ejecuta Uvicorn con la opción --reload para facilitar el desarrollo.

## Levantar solamente la configuración base

Para ejecutar solamente el archivo principal sin aplicar el override:

docker-compose -f docker-compose.yml up --build -d

## Verificar los contenedores

docker-compose ps

Los servicios deben aparecer como healthy.

## Detener los servicios

docker-compose down

Los volúmenes no se eliminan, por lo que los datos permanecen almacenados.

## Endpoint principal

GET /

http://localhost:8000/

Permite comprobar que la aplicación FastAPI se encuentra activa.

## Healthcheck

GET /health

http://localhost:8000/health

Comprueba la conectividad con Redis y PostgreSQL.

Respuesta esperada:

{
  "status": "healthy",
  "redis": "OK",
  "postgresql": "OK"
}

## Contador con Redis

GET /contador

http://localhost:8000/contador

El contador utiliza la operación INCR de Redis.

Cada solicitud aumenta el valor almacenado.

Ejemplo:

{
  "visitas": 3
}

## Consulta de usuarios

GET /usuarios

http://localhost:8000/usuarios

El funcionamiento del endpoint es:

1. FastAPI consulta Redis.
2. Si los usuarios están almacenados en caché, devuelve los datos desde Redis.
3. Si la caché no existe, consulta PostgreSQL.
4. Los resultados de PostgreSQL se almacenan temporalmente en Redis.

Ejemplo de primera consulta:

{
  "origen": "postgresql",
  "usuarios": []
}

Ejemplo de segunda consulta:

{
  "origen": "cache",
  "usuarios": []
}

## Limpiar caché

DELETE /cache

http://localhost:8000/cache

Elimina la clave utilizada para almacenar los usuarios en Redis.

También puede realizarse directamente mediante:

docker exec redis_cache redis-cli DEL usuarios_cache

## Rate Limiting

La aplicación limita las solicitudes a un máximo de 10 peticiones por minuto por dirección IP.

Cuando se supera el límite, la API devuelve:

HTTP 429 Too Many Requests

Respuesta:

{
  "detail": "Limite de 10 solicitudes por minuto excedido"
}

## PostgreSQL

PostgreSQL contiene la tabla:

usuarios

La tabla se crea automáticamente mediante:

db/init.sql

Los datos de PostgreSQL se almacenan en el volumen:

escenario3_pg_data

## Redis

Redis utiliza persistencia mediante AOF.

Los datos se almacenan en el volumen:

escenario3_redis_data

Redis se utiliza para:

- Caché de usuarios
- Contador de visitas
- Rate limiting

## Red Docker

Los servicios se comunican mediante:

escenario3_cache_network

## Persistencia

Se comprobó la persistencia deteniendo los servicios con:

docker-compose down

y volviéndolos a crear con:

docker-compose up -d

Los registros almacenados en PostgreSQL continuaron disponibles después del reinicio.

El contador almacenado en Redis también conservó su valor.

## Documentación FastAPI

FastAPI genera automáticamente documentación interactiva disponible en:

http://localhost:8000/docs