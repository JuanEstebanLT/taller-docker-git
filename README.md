# Taller Práctico: Docker + Git + Kubernetes

Este repositorio contiene el desarrollo del Taller Práctico de Docker + Git, organizado en cuatro escenarios progresivos, más la documentación y manifiestos de **Kubernetes, kubectl y Minikube**.

## Escenarios

1. Escenario 1: WordPress + Base de datos
2. Escenario 2: API REST Node.js + PostgreSQL
3. Escenario 3: Aplicación con caché Redis
4. Escenario 4: CI/CD con GitHub Actions y DockerHub

## Kubernetes y Minikube

Guía conceptual, referencia de comandos y YAML comentado:

- Índice: [`docs/kubernetes/README.md`](docs/kubernetes/README.md)
- Manifiestos: [`k8s/`](k8s/)

Documentación auxiliar de Docker y Git:

- [`docs/docker-commands.md`](docs/docker-commands.md)
- [`docs/git-workflow.md`](docs/git-workflow.md)

## Estrategia de ramas

- `main`: documentación general del proyecto.
- `escenario-1-wordpress`: desarrollo del escenario 1.
- `escenario-2-api-node`: desarrollo del escenario 2.
- `escenario-3-redis`: desarrollo del escenario 3.
- `escenario-4-cicd`: desarrollo del escenario 4.
- `docs/kubernetes-minikube`: documentación y manifiestos de Kubernetes / Minikube.

## Flujo de trabajo

Cada escenario se desarrolla en su propia rama.

Al finalizar un escenario se realiza un commit descriptivo y se sube la rama al repositorio remoto.