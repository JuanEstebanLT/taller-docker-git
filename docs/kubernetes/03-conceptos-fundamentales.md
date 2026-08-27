# 1.4 Conceptos fundamentales de Kubernetes

## Pod

Es la **unidad mínima desplegable** en Kubernetes. Un Pod puede contener uno o más contenedores que:

- Comparten la misma dirección IP.
- Comparten volúmenes de almacenamiento.
- Se ejecutan en el mismo contexto de red.

Un Pod es como una cápsula espacial: dentro pueden viajar uno o más astronautas (contenedores) que comparten recursos y espacio vital.

En la práctica, lo habitual es **un contenedor de aplicación por Pod**. Los sidecar (logs, proxy, sync) se agregan cuando hace falta compartir red o disco.

Los Pods son **efímeros**: si mueren, su IP cambia. Por eso no se accede a ellos por IP directa en producción, sino a través de un Service.

## Service

Proporciona una **interfaz de red estable** para acceder a un conjunto de Pods. Como los Pods son efímeros (sus IPs cambian), el Service actúa como punto de acceso fijo (IP virtual + DNS interno).

### Tipos de Service

| Tipo | Uso |
| --- | --- |
| **ClusterIP** | Accesible solo dentro del cluster. Es el tipo por defecto. |
| **NodePort** | Expone el servicio en un puerto de cada nodo (rango 30000–32767). |
| **LoadBalancer** | Crea un balanceador externo (típico en la nube). En Minikube se usa `minikube tunnel`. |
| **ExternalName** | Mapea el Service a un nombre DNS externo (CNAME). |

Flujo de un Service **NodePort**:

```
Usuario / Cliente
        │
        ▼
Nodo:puerto 30080     ← nodePort (acceso externo)
        │
        ▼
Service:puerto 80     ← port (acceso interno del cluster)
        │
        ▼
Pod:puerto 80         ← targetPort (contenedor)
```

## Deployment

Gestiona la creación y actualización de **ReplicaSets**, que a su vez gestionan Pods. Proporciona:

- Declaración del estado deseado.
- Replicación automática.
- Rolling updates y rollbacks.
- Auto-recuperación (si un Pod muere, se crea otro).

No se suele crear un Pod “suelto” en producción: se declara un Deployment y Kubernetes mantiene el número de réplicas.

## Namespace

Proporciona **aislamiento lógico** dentro de un cluster. Permite dividir recursos entre diferentes equipos, proyectos o entornos (`dev`, `staging`, `prod`).

Namespaces predeterminados:

- `default`
- `kube-system`
- `kube-public`
- `kube-node-lease`

Los recursos se identifican de forma única por la combinación **kind + metadata.name + metadata.namespace**.

## ConfigMap y Secret

- **ConfigMap:** almacena configuración no sensible (variables de entorno, archivos de configuración).
- **Secret:** almacena información sensible (contraseñas, tokens, claves SSH) en base64.

Un Secret en base64 **no es cifrado**. Cualquiera con permiso de lectura en el cluster puede decodificarlo. En producción se combinan RBAC, cifrado en etcd y gestores externos (por ejemplo Sealed Secrets o un vault).

## Otros recursos frecuentes

| Recurso | Rol |
| --- | --- |
| **ReplicaSet** | Mantiene N copias de un Pod. Lo gestiona el Deployment. |
| **StatefulSet** | Apps con identidad estable (bases de datos). |
| **DaemonSet** | Un Pod por nodo (agentes, logs, red). |
| **Job / CronJob** | Tareas que terminan, o tareas programadas. |
| **Ingress** | Enrutamiento HTTP/HTTPS hacia Services. |
| **PersistentVolumeClaim** | Solicitud de almacenamiento persistente. |
| **HorizontalPodAutoscaler** | Escala réplicas según CPU/memoria u otras métricas. |
