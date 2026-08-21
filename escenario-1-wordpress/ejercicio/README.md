# Escenario 1: WordPress + MariaDB

Este escenario implementa WordPress utilizando MariaDB como base de datos y phpMyAdmin para la administración de la base de datos.

## Servicios

- WordPress
- MariaDB
- phpMyAdmin

## Puertos

- WordPress: http://localhost:8080
- phpMyAdmin: http://localhost:8081

## Levantar los servicios

Ubicarse en la carpeta:

escenario-1-wordpress/ejercicio

Ejecutar:

docker-compose up -d

## Verificar los servicios

docker-compose ps

## Ver los logs

docker-compose logs -f

## Detener los servicios

docker-compose down

## Detener los servicios y eliminar los volúmenes

docker-compose down -v