# Flujo de trabajo típico (Minikube + kubectl)

## 1. Iniciar Minikube

```bash
minikube start --driver=docker
```

## 2. Verificar el cluster

```bash
kubectl get nodes
kubectl cluster-info
```

## 3. Crear recursos desde YAML

Desde la raíz del repositorio:

```bash
kubectl apply -f k8s/manifests/namespace.yaml
kubectl apply -f k8s/manifests/configmap.yaml
kubectl apply -f k8s/manifests/secret.yaml
kubectl apply -f k8s/manifests/deployment.yaml
kubectl apply -f k8s/manifests/service-nodeport.yaml
```

O todo el directorio (el namespace debe existir primero; `namespace.yaml` está pensado para aplicarse junto al resto si Kubernetes crea dependencias en paralelo, pero conviene el orden de arriba):

```bash
kubectl apply -f k8s/manifests/
```

## 4. Comprobar

```bash
kubectl get all -n taller-k8s
kubectl get pods -n taller-k8s
kubectl describe pod -n taller-k8s -l app=nginx
```

## 5. Logs y shell

```bash
kubectl logs -n taller-k8s -l app=nginx
kubectl exec -it -n taller-k8s deploy/nginx-deployment -- /bin/sh
```

## 6. Exponer el Service (NodePort)

```bash
minikube service mi-servicio-nginx -n taller-k8s --url
```

## 7. Escalar

```bash
kubectl scale deployment nginx-deployment -n taller-k8s --replicas=5
```

## 8. Actualizar la aplicación

```bash
kubectl set image deployment/nginx-deployment nginx=nginx:1.25-alpine -n taller-k8s
kubectl rollout status deployment/nginx-deployment -n taller-k8s
```

## 9. Rollback si falla

```bash
kubectl rollout undo deployment/nginx-deployment -n taller-k8s
```

## 10. Limpiar

```bash
kubectl delete -f k8s/manifests/
# o
minikube delete
```

Los recursos se identifican por `apiVersion`, `kind` y `metadata.name`. La combinación de **kind + metadata.name + metadata.namespace** debe ser única en el cluster.
