# Comandos Docker

## Levantar servicios

docker-compose up -d

## Reconstruir imágenes

docker-compose up --build -d

## Ver estado

docker-compose ps

## Ver logs

docker-compose logs -f

## Detener servicios

docker-compose stop

## Iniciar servicios

docker-compose start

## Eliminar servicios

docker-compose down

## Eliminar servicios y volúmenes

docker-compose down -v

## Entrar a un servicio

docker-compose exec servicio sh