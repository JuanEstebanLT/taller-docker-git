# 1.3 Arquitectura de Kubernetes

Kubernetes opera como un **cluster** (conjunto de máquinas) dividido en dos tipos de nodos: el **nodo Master (Control Plane)** y los **nodos Worker**.

```
                    CONTROL PLANE (Master)
        ┌──────────────────────────────────────────┐
        │  API Server   Scheduler   Controllers    │
        │              etcd                        │
        └──────────────────┬───────────────────────┘
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
         Worker 1     Worker 2     Worker N
         kubelet      kubelet      kubelet
         kube-proxy   kube-proxy   kube-proxy
         runtime      runtime      runtime
            │            │            │
          Pods         Pods         Pods
```

## Nodo Master (Control Plane)

Es el cerebro del cluster. Gestiona el estado del sistema y toma decisiones. Sus componentes principales son:

| Componente | Función |
| --- | --- |
| **API Server** (`kube-apiserver`) | Punto de entrada para todas las operaciones. Recibe comandos de `kubectl` y los valida. |
| **etcd** | Base de datos distribuida que almacena toda la configuración y el estado del cluster. |
| **Scheduler** (`kube-scheduler`) | Decide en qué nodo worker se ejecutará cada Pod, basándose en recursos disponibles. |
| **Controller Manager** (`kube-controller-manager`) | Ejecuta controladores que monitorean el estado y realizan acciones correctivas. |
| **Cloud Controller Manager** | Integra Kubernetes con proveedores de nube (AWS, Azure, GCP). |

## Nodos Worker

Ejecutan las aplicaciones (los Pods). Cada worker incluye:

| Componente | Función |
| --- | --- |
| **kubelet** | Agente en el nodo. Habla con el API Server y se asegura de que los contenedores descritos en cada Pod estén corriendo. |
| **kube-proxy** | Mantiene las reglas de red del nodo para que los Services enruten tráfico a los Pods correctos. |
| **Container Runtime** | Motor que realmente ejecuta contenedores (containerd, CRI-O u otros compatibles con CRI). |

En **Minikube** el Control Plane y el Worker suelen vivir en **un solo nodo** local. El modelo conceptual es el mismo que en un cluster de producción.
