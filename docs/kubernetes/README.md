# Documentación Kubernetes + Minikube

Material del taller a partir de las guías **Kubernetes y Minikube** (conceptos) y **Referencia rápida: Kubernetes, kubectl, Minikube y YAML** (comandos y manifiestos).

## Contenido

1. [¿Qué es Kubernetes?](01-que-es-kubernetes.md)
2. [Arquitectura del cluster](02-arquitectura.md)
3. [Conceptos fundamentales](03-conceptos-fundamentales.md)
4. [Imperativo vs declarativo](04-imperativo-vs-declarativo.md)
5. [Minikube](05-minikube.md)
6. [kubectl](06-kubectl.md)
7. [Referencia de comandos kubectl](07-referencia-kubectl.md)
8. [Referencia de comandos Minikube](08-referencia-minikube.md)
9. [Manifiestos YAML línea por línea](09-manifiestos-yaml.md)
10. [Flujo de trabajo típico](10-flujo-de-trabajo.md)

## Manifiestos de práctica

Los YAML aplican un Deployment de nginx en el namespace `taller-k8s`, con ConfigMap, Secret de ejemplo, Service NodePort, PVC, HPA e Ingress.

```bash
minikube start --driver=docker
minikube addons enable metrics-server
minikube addons enable ingress
kubectl apply -f k8s/manifests/
kubectl get all -n taller-k8s
minikube service mi-servicio-nginx -n taller-k8s --url
```
