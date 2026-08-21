# Escenario 4: CI/CD con GitHub Actions y Docker

![CI/CD](https://github.com/JuanEstebanLT/taller-docker-git/actions/workflows/ci-cd.yml/badge.svg?branch=escenario-4-cicd)

Este escenario implementa un pipeline de integración y entrega continua para una aplicación desarrollada con FastAPI.

El pipeline ejecuta pruebas automatizadas, construye una imagen Docker, realiza un análisis de seguridad con Trivy y publica la imagen en Docker Hub y GitHub Container Registry.

## Tecnologías

- Python 3.11
- FastAPI
- Pytest
- Docker
- Docker Compose
- GitHub Actions
- Docker Hub
- GitHub Container Registry
- Trivy

## Estructura

escenario-4-cicd/ejercicio/

Dockerfile

docker-compose.yml

docker-compose.prod.yml

requirements.txt

README.md

src/
    main.py

tests/
    test_app.py

El workflow se encuentra en la raíz del repositorio:

.github/workflows/ci-cd.yml

## Endpoints

### Inicio

GET /

http://localhost:8000/

Respuesta:

{
  "mensaje": "API CI/CD funcionando",
  "version": "1.0.0"
}

### Healthcheck

GET /health

http://localhost:8000/health

Respuesta:

{
  "status": "healthy"
}

### Información

GET /info

http://localhost:8000/info

## Pruebas

Las pruebas automatizadas se encuentran en:

tests/test_app.py

Se comprueban:

- Endpoint principal.
- Healthcheck.
- Endpoint de información.
- Respuesta 404 para una ruta inexistente.

Las pruebas se ejecutan antes de construir y publicar la imagen Docker.

## Docker

Para construir y ejecutar localmente:

docker-compose up --build -d

Para verificar:

docker-compose ps

Para detener:

docker-compose down

## Dockerfile multi-stage

La aplicación utiliza un Dockerfile multi-stage.

La primera etapa instala las dependencias.

La segunda etapa contiene solamente los componentes necesarios para ejecutar la aplicación.

## Pipeline CI/CD

El workflow se encuentra en:

.github/workflows/ci-cd.yml

El flujo ejecutado es:

1. Descargar el repositorio.
2. Configurar Python.
3. Instalar dependencias.
4. Ejecutar las pruebas con pytest.
5. Construir la imagen Docker.
6. Analizar la imagen con Trivy.
7. Publicar la imagen cuando se utiliza un tag de versión.

La construcción depende de que las pruebas sean exitosas.

## Seguridad

Trivy analiza la imagen Docker buscando vulnerabilidades de severidad HIGH y CRITICAL.

## Docker Hub

La imagen se publica en:

play1501/api-cicd

## GitHub Container Registry

La misma imagen también es publicada en GitHub Container Registry.

## Versionado

El proyecto utiliza versionado semántico.

Ejemplo:

v1.0.0

Al publicar esa versión se generan las etiquetas:

v1.0.0

v1.0

latest

## Producción

El archivo:

docker-compose.prod.yml

permite ejecutar la imagen previamente publicada en el registro en lugar de construirla localmente.

## Documentación de FastAPI

La documentación interactiva puede consultarse en:

http://localhost:8000/docs