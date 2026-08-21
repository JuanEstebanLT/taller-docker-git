# Escenario 2: API REST Node.js + PostgreSQL

Este escenario implementa una API REST desarrollada con Node.js y Express, conectada a una base de datos PostgreSQL y ejecutada mediante Docker Compose.

## Servicios

- API Node.js
- PostgreSQL
- pgAdmin

## Puertos

- API Node.js: http://localhost:3000
- pgAdmin: http://localhost:5050

## Endpoints

### Verificar estado de la API

GET /health

http://localhost:3000/health

### Obtener usuarios

GET /usuarios

http://localhost:3000/usuarios

### Crear usuario

POST /usuarios

Ejemplo:

{
  "nombre": "Juan",
  "email": "juan@test.com"
}

### Actualizar usuario

PUT /usuarios/:id

Ejemplo:

{
  "nombre": "Juan Esteban",
  "email": "juanesteban@test.com"
}

### Eliminar usuario

DELETE /usuarios/:id

## Levantar los servicios

Ubicarse en:

escenario-2-api-node/ejercicio

Ejecutar:

docker-compose up --build -d

## Verificar los servicios

docker-compose ps

## Ver logs

docker-compose logs -f

## Detener los servicios

docker-compose down

## pgAdmin

Acceder a:

http://localhost:5050

Datos de conexión al servidor PostgreSQL:

Host: db
Puerto: 5432
Base de datos: apidb
Usuario: postgres

## Persistencia

PostgreSQL utiliza un volumen Docker para conservar la información aunque los contenedores sean detenidos y creados nuevamente.

## Migración

El archivo:

init-scripts/01-init.sql

crea automáticamente la tabla usuarios cuando PostgreSQL inicializa la base de datos por primera vez.