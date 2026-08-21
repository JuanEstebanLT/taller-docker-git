from fastapi import FastAPI

app = FastAPI(
    title="API CI/CD",
    version="1.0.0"
)


@app.get("/")
def inicio():
    return {
        "mensaje": "API CI/CD funcionando",
        "version": "1.0.0"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/info")
def info():
    return {
        "aplicacion": "API FastAPI CI/CD",
        "version": "1.0.0",
        "entorno": "Docker"
    }