# Referencia rápida: comandos de kubectl

`kubectl` es la herramienta de línea de comandos oficial para interactuar con clusters Kubernetes.

## 1.1 Información del cluster

| Comando | Explicación |
| --- | --- |
| `kubectl cluster-info` | Muestra la dirección del API Server y los servicios principales del cluster. Útil para verificar conectividad. |
| `kubectl version` | Muestra la versión del cliente (`kubectl`) y del servidor (API Server). Ayuda a detectar incompatibilidades. |
| `kubectl get nodes` | Lista todos los nodos del cluster con su estado (`Ready`, `NotReady`), versión y tiempo de actividad. |
| `kubectl get nodes -o wide` | Información extendida: IP interna, IP externa, sistema operativo, kernel. |
| `kubectl describe node <nombre>` | Detalles del nodo: capacidad de CPU/memoria, Pods asignados, eventos, condiciones. |

## 1.2 Gestión de Pods

| Comando | Explicación |
| --- | --- |
| `kubectl get pods` | Lista los Pods del namespace por defecto (`default`). Nombre, estado, reinicios y edad. |
| `kubectl get pods -n <namespace>` | Pods de un namespace. Ejemplo: `kubectl get pods -n kube-system`. |
| `kubectl get pods -o wide` | Extra: IP del Pod, nodo, IPs de contenedores. |
| `kubectl get pods --all-namespaces` | Pods de todos los namespaces. |
| `kubectl get pods -l app=nginx` | Filtra por labels. Solo los que tengan `app=nginx`. |
| `kubectl describe pod <nombre>` | Eventos, condiciones, volúmenes, contenedores, IPs. |
| `kubectl logs <nombre-pod>` | stdout/stderr de un Pod de un solo contenedor. |
| `kubectl logs <nombre-pod> -c <contenedor>` | Logs de un contenedor concreto (Pods multi-contenedor). |
| `kubectl logs <nombre-pod> -f` | Sigue los logs en tiempo real (como `tail -f`). |
| `kubectl logs <nombre-pod> --previous` | Logs del contenedor anterior (útil tras un crash/reinicio). |
| `kubectl exec -it <nombre-pod> -- /bin/sh` | Shell interactiva. `-it` = interactivo + TTY. |
| `kubectl exec -it <nombre-pod> -- /bin/bash` | Igual con Bash, si la imagen lo incluye. |
| `kubectl exec <nombre-pod> -- ls /` | Un comando único, sin shell interactiva. |
| `kubectl port-forward <nombre-pod> 8080:80` | Puerto 80 del Pod → 8080 en tu máquina. |
| `kubectl delete pod <nombre>` | Elimina el Pod. Si pertenece a un Deployment, Kubernetes lo recrea. |
| `kubectl delete pod <nombre> --force --grace-period=0` | Eliminación inmediata, sin período de gracia. |

## 1.3 Gestión de Deployments

| Comando | Explicación |
| --- | --- |
| `kubectl get deployments` | Réplicas deseadas, actuales, disponibles y edad. |
| `kubectl get deployments -o wide` | Información extendida. |
| `kubectl describe deployment <nombre>` | Estrategia, selector, condiciones, eventos, réplicas. |
| `kubectl create deployment <nombre> --image=<imagen>` | Creación imperativa. Ejemplo: `kubectl create deploy nginx --image=nginx`. |
| `kubectl apply -f deployment.yaml` | Crea o actualiza desde YAML declarativo. |
| `kubectl delete deployment <nombre>` | Elimina el Deployment y sus Pods. |
| `kubectl scale deployment <nombre> --replicas=5` | Cambia el número de réplicas. |
| `kubectl autoscale deployment <nombre> --min=2 --max=10 --cpu-percent=80` | Configura HPA según CPU. |
| `kubectl rollout status deployment/<nombre>` | Estado de un rolling update. |
| `kubectl rollout history deployment/<nombre>` | Historial de revisiones. |
| `kubectl rollout history deployment/<nombre> --revision=2` | Detalle de una revisión. |
| `kubectl set image deployment/<nombre> <contenedor>=<nueva-imagen>` | Cambia la imagen e inicia rolling update. |
| `kubectl rollout undo deployment/<nombre>` | Rollback a la revisión anterior. |
| `kubectl rollout undo deployment/<nombre> --to-revision=1` | Rollback a una revisión concreta. |
| `kubectl rollout pause deployment/<nombre>` | Pausa un despliegue en curso. |
| `kubectl rollout resume deployment/<nombre>` | Reanuda un despliegue pausado. |

## 1.4 Gestión de Services

| Comando | Explicación |
| --- | --- |
| `kubectl get services` | Tipo (ClusterIP, NodePort, LoadBalancer), IP interna y puertos. |
| `kubectl get svc` | Alias de `kubectl get services`. |
| `kubectl get svc -o wide` | Información extendida. |
| `kubectl describe service <nombre>` | Selector, endpoints, puertos, IPs, eventos. |
| `kubectl apply -f service.yaml` | Crea o actualiza desde YAML. |
| `kubectl delete service <nombre>` | Quita el Service; los Pods siguen corriendo. |
| `kubectl get endpoints <nombre-svc>` | IPs y puertos de los Pods detrás del Service. |
| `kubectl expose deployment <nombre> --type=NodePort --port=80` | Expone un Deployment de forma imperativa. |

## 1.5 Gestión de namespaces

| Comando | Explicación |
| --- | --- |
| `kubectl get namespaces` | Lista namespaces, incluidos `default`, `kube-system`, `kube-public`, `kube-node-lease`. |
| `kubectl create namespace <nombre>` | Crea un namespace. |
| `kubectl delete namespace <nombre>` | Elimina el namespace y **todo** lo que contiene. Irreversible. |
| `kubectl config set-context --current --namespace=<nombre>` | Namespace por defecto para los siguientes comandos. |
| `kubectl get all -n <nombre>` | Pods, Services, Deployments y ReplicaSets del namespace. |

## 1.6 ConfigMaps y Secrets

| Comando | Explicación |
| --- | --- |
| `kubectl get configmaps` | Lista ConfigMaps (configuración no sensible). |
| `kubectl get secrets` | Lista Secrets (datos sensibles). |
| `kubectl describe configmap <nombre>` | Claves y valores del ConfigMap. |
| `kubectl describe secret <nombre>` | Metadatos. El contenido está en base64. |
| `kubectl create configmap <nombre> --from-literal=clave=valor` | Desde pares clave-valor. |
| `kubectl create configmap <nombre> --from-file=archivo.properties` | Desde un archivo. |
| `kubectl create secret generic <nombre> --from-literal=password=secreto` | Secret genérico; se codifica en base64. |
| `kubectl create secret tls <nombre> --cert=cert.pem --key=key.pem` | Secret TLS. |
| `kubectl delete configmap <nombre>` | Elimina un ConfigMap. |
| `kubectl delete secret <nombre>` | Elimina un Secret. |

## 1.7 Comandos generales

| Comando | Explicación |
| --- | --- |
| `kubectl apply -f <archivo.yaml>` | Crea o actualiza recursos. Idempotente. |
| `kubectl apply -f <directorio>/` | Aplica todos los YAML de un directorio. |
| `kubectl delete -f <archivo.yaml>` | Elimina los recursos del archivo. |
| `kubectl get all` | Recursos principales del namespace actual. |
| `kubectl get all -n <namespace>` | Recursos de un namespace. |
| `kubectl get events` | Eventos recientes (errores, creaciones, eliminaciones). |
| `kubectl get events --sort-by='.lastTimestamp'` | Eventos ordenados por fecha. |
| `kubectl top nodes` | CPU y memoria de nodos (requiere Metrics Server). |
| `kubectl top pods` | CPU y memoria de Pods (requiere Metrics Server). |
| `kubectl explain pod` | Documentación del recurso Pod. |
| `kubectl explain pod.spec` | Documentación de un campo. |
| `kubectl explain deployment.spec.replicas` | Campo anidado. |
| `kubectl cp <archivo-local> <pod>:<ruta-destino>` | Copia local → Pod. |
| `kubectl cp <pod>:<ruta-origen> <archivo-local>` | Copia Pod → local. |
