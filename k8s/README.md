# Manifiestos Kubernetes

## `manifests/`

Conjunto coherente para aplicar en Minikube (namespace `taller-k8s`):

- Namespace, ConfigMap, Secret de laboratorio
- Deployment de nginx (3 réplicas, probes y recursos)
- Service NodePort (`30080`) y ClusterIP
- PVC, HPA e Ingress

```bash
kubectl apply -f k8s/manifests/
```

El Secret usa `stringData` con valores ficticios. No coloques tokens reales en estos archivos.

## `ejemplos/`

Pod suelto del material de referencia. No forma parte del Deployment; aplícalo solo si quieres comparar un Pod autónomo con uno gestionado:

```bash
kubectl apply -f k8s/ejemplos/pod.yaml
```
