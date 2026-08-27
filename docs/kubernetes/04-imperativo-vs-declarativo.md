# Enfoque imperativo vs declarativo

Kubernetes se puede administrar de dos formas. El taller usa ambas: comandos rápidos para explorar, y YAML para dejar el estado versionado en Git.

| Enfoque | Descripción | Ejemplo |
| --- | --- | --- |
| **Imperativo** | Le dices a Kubernetes **qué** hacer, paso a paso. | `kubectl run nginx --image=nginx` |
| **Declarativo** | Le dices a Kubernetes **cómo** quieres que sea el estado final. | `kubectl apply -f deployment.yaml` |

Kubernetes favorece el enfoque **declarativo**, ya que permite:

- **Versionado de configuraciones (GitOps):** los manifiestos viven en el repositorio.
- **Replicabilidad:** el mismo YAML se aplica en otro cluster.
- **Recuperación ante desastres:** se vuelve a aplicar el estado deseado.
- **Colaboración en equipos:** el cambio se revisa en un pull request.

`kubectl apply` es **idempotente**: se puede ejecutar varias veces; Kubernetes solo cambia lo que difiere del estado actual.

En este repositorio los manifiestos de ejemplo están en [`k8s/manifests/`](../../k8s/manifests/).
