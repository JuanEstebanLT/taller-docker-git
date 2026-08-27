# Manifiestos YAML, línea por línea

Los recursos se identifican por `apiVersion`, `kind` y `metadata.name`. La combinación **kind + name + namespace** debe ser única en el cluster.

Los archivos listos para aplicar están en [`k8s/manifests/`](../../k8s/manifests/).

## 3.1 Pod

```yaml
apiVersion: v1                 # Versión de la API de Kubernetes para Pods
kind: Pod                      # Tipo de recurso: unidad mínima desplegable
metadata:                      # Metadatos del recurso
  name: mi-primer-pod          # Nombre único dentro del namespace
  labels:                      # Etiquetas para identificar y agrupar
    app: nginx                 # Label clave-valor: app=nginx
    tier: frontend             # Label adicional
spec:                          # Qué debe contener el Pod
  containers:                  # Lista de contenedores
    - name: nginx              # Nombre único dentro del Pod
      image: nginx:1.25        # Imagen Docker (nombre:tag)
      ports:
        - containerPort: 80    # Puerto HTTP del contenedor
      env:
        - name: MI_VARIABLE
          value: "hola"
      resources:
        requests:              # Mínimo garantizado
          memory: "64Mi"
          cpu: "250m"          # 250 milicores = 0.25 CPU
        limits:                # Máximo permitido
          memory: "128Mi"
          cpu: "500m"
```

## 3.2 Service (NodePort)

```yaml
apiVersion: v1
kind: Service
metadata:
  name: mi-servicio-nginx
  namespace: default
spec:
  type: NodePort               # Expone un puerto en cada nodo
  selector:
    app: nginx                 # Pods con label app=nginx
  ports:
    - port: 80                 # Puerto interno del Service
      targetPort: 80           # Puerto del contenedor
      nodePort: 30080          # Puerto en el nodo (30000-32767)
      protocol: TCP
```

Flujo: cliente → `nodo:30080` (nodePort) → Service `:80` (port) → Pod `:80` (targetPort).

## 3.3 Service (ClusterIP)

```yaml
apiVersion: v1
kind: Service
metadata:
  name: mi-servicio-interno
spec:
  type: ClusterIP              # Solo accesible dentro del cluster
  selector:
    app: backend
  ports:
    - port: 8080
      targetPort: 80
```

DNS interno: `mi-servicio-interno` (mismo namespace) o `mi-servicio-interno.default.svc.cluster.local`.

## 3.4 Deployment

```yaml
apiVersion: apps/v1            # API estable de Deployments
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3                  # Pods que debe mantener
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1              # Pods extra durante la actualización
      maxUnavailable: 0        # Ningún Pod caído a la vez
  selector:
    matchLabels:
      app: nginx               # Debe coincidir con los labels del template
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: nginx:1.25
          ports:
            - containerPort: 80
          livenessProbe:       # ¿Sigue vivo el contenedor?
            httpGet:
              path: /
              port: 80
            initialDelaySeconds: 10
            periodSeconds: 10
          readinessProbe:      # ¿Puede recibir tráfico?
            httpGet:
              path: /
              port: 80
            initialDelaySeconds: 5
            periodSeconds: 5
```

## 3.5 ConfigMap

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: mi-configuracion
  namespace: default
data:
  database.properties: |
    host=localhost
    port=5432
    name=mibase
  modo_debug: "true"
  max_conexiones: "100"        # En ConfigMap los valores son strings
```

Uso en un Pod: variables de entorno (`configMapKeyRef`) o volumen (`volumes.configMap`).

## 3.6 Secret

Los valores en `data` van en **base64**. Para codificar:

```bash
echo -n "secreto123" | base64
```

También se puede usar `stringData` (texto plano; Kubernetes lo convierte):

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: mis-secretos
type: Opaque
stringData:
  password: secreto123
  token: mi-token-secreto
```

Estos valores son de **ejemplo de laboratorio**. No uses contraseñas reales ni tokens de GitHub en manifiestos.

## 3.7 Namespace

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: produccion
  labels:
    entorno: prod
    equipo: backend
```

## 3.8 HorizontalPodAutoscaler (HPA)

Requiere Metrics Server (`minikube addons enable metrics-server`).

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: nginx-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: nginx-deployment
  minReplicas: 2
  maxReplicas: 10
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
    - type: Resource
      resource:
        name: memory
        target:
          type: Utilization
          averageUtilization: 80
```

## 3.9 Ingress

Requiere `minikube addons enable ingress`.

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: mi-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
    - host: miapp.local
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: mi-servicio-nginx
                port:
                  number: 80
    - host: api.local
      http:
        paths:
          - path: /api
            pathType: Prefix
            backend:
              service:
                name: api-service
                port:
                  number: 8080
```

## 3.10 PersistentVolumeClaim (PVC)

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: mi-volumen
spec:
  accessModes:
    - ReadWriteOnce            # Un nodo lee y escribe
  resources:
    requests:
      storage: 1Gi
  storageClassName: standard
```

En el Pod se monta con `volumes.persistentVolumeClaim.claimName`.

## Tabla de recursos y apiVersion

| Recurso | apiVersion | kind | Descripción |
| --- | --- | --- | --- |
| Pod | `v1` | Pod | Unidad mínima desplegable |
| Service | `v1` | Service | Exposición de red estable |
| ConfigMap | `v1` | ConfigMap | Configuración no sensible |
| Secret | `v1` | Secret | Datos sensibles (base64) |
| Namespace | `v1` | Namespace | Aislamiento lógico |
| PersistentVolumeClaim | `v1` | PersistentVolumeClaim | Solicitud de almacenamiento |
| Deployment | `apps/v1` | Deployment | Gestión declarativa de la app |
| ReplicaSet | `apps/v1` | ReplicaSet | Réplicas (lo gestiona el Deployment) |
| StatefulSet | `apps/v1` | StatefulSet | Apps con estado |
| DaemonSet | `apps/v1` | DaemonSet | Un Pod por nodo |
| Job | `batch/v1` | Job | Tarea hasta completarse |
| CronJob | `batch/v1` | CronJob | Tarea periódica |
| Ingress | `networking.k8s.io/v1` | Ingress | Enrutamiento HTTP/HTTPS |
| NetworkPolicy | `networking.k8s.io/v1` | NetworkPolicy | Firewall entre Pods |
| HorizontalPodAutoscaler | `autoscaling/v2` | HorizontalPodAutoscaler | Escalado automático |
| ServiceAccount | `v1` | ServiceAccount | Identidad para Pods |
| Role | `rbac.authorization.k8s.io/v1` | Role | Permisos en un namespace |
| ClusterRole | `rbac.authorization.k8s.io/v1` | ClusterRole | Permisos a nivel de cluster |
