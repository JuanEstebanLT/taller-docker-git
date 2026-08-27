# 2.5 kubectl: la interfaz de línea de comandos

`kubectl` es la herramienta oficial de línea de comandos para interactuar con clusters Kubernetes. Funciona como el **control remoto** del cluster: habla con el API Server, nunca modifica etcd ni los nodos de forma directa.

## Sintaxis básica

```text
kubectl [comando] [tipo-de-recurso] [nombre-del-recurso] [flags]
```

Ejemplos:

```bash
kubectl get pods                    # Listar Pods
kubectl get pods -o wide            # Listar Pods con más detalles
kubectl describe pod mi-pod         # Ver detalles de un Pod
kubectl logs mi-pod                 # Ver logs de un Pod
kubectl exec -it mi-pod -- /bin/sh  # Acceder a un Pod
kubectl apply -f archivo.yaml       # Aplicar configuración declarativa
kubectl delete -f archivo.yaml      # Eliminar recursos
```

Alias frecuentes:

| Corto | Completo |
| --- | --- |
| `po` | `pods` |
| `svc` | `services` |
| `deploy` | `deployments` |
| `ns` | `namespaces` |
| `cm` | `configmaps` |

La referencia detallada (cluster, Pods, Deployments, Services, namespaces, ConfigMaps, Secrets y utilidades) está en [`07-referencia-kubectl.md`](07-referencia-kubectl.md).
