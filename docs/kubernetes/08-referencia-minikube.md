# Referencia rápida: comandos de Minikube

Minikube ejecuta un cluster Kubernetes de un solo nodo en local.

| Comando | Explicación |
| --- | --- |
| `minikube start` | Inicia un cluster. Si ya existe, lo reanuda. |
| `minikube start --driver=docker` | Driver Docker (más ligero que una VM). |
| `minikube start --driver=hyperv` | Driver Hyper-V (Windows). |
| `minikube start --driver=virtualbox` | Driver VirtualBox. |
| `minikube start --cpus=4 --memory=8192` | 4 CPU y 8 GB de RAM. |
| `minikube start --kubernetes-version=v1.28.0` | Versión concreta de Kubernetes. |
| `minikube stop` | Detiene el cluster y conserva el estado. |
| `minikube delete` | Elimina el cluster y todos sus recursos. |
| `minikube status` | Si está corriendo, driver y versión. |
| `minikube ip` | IP del nodo. Útil para Services NodePort. |
| `minikube ssh` | SSH dentro de la VM o contenedor de Minikube. |
| `minikube dashboard` | Abre el dashboard web de Kubernetes. |
| `minikube service <nombre-servicio>` | Abre un Service NodePort/LoadBalancer en el navegador. |
| `minikube service <nombre-servicio> --url` | Muestra la URL sin abrir el navegador. |
| `minikube addons list` | Add-ons y su estado. |
| `minikube addons enable <nombre>` | Ejemplo: `minikube addons enable ingress`. |
| `minikube addons disable <nombre>` | Deshabilita un add-on. |
| `minikube addons enable metrics-server` | Necesario para `kubectl top`. |
| `minikube addons enable ingress` | Controlador Ingress HTTP/HTTPS. |
| `minikube tunnel` | Túnel para Services tipo LoadBalancer en local. |
| `minikube profile list` | Perfiles (clusters) existentes. |
| `minikube profile <nombre>` | Cambia de perfil. |
| `minikube update-check` | Comprueba si hay versión nueva. |
| `minikube version` | Versión instalada. |
| `minikube docker-env` | Variables para usar el Docker interno de Minikube. |
| `eval $(minikube docker-env)` | Linux/macOS: apunta el Docker client al daemon de Minikube. |
| `minikube image load <imagen>` | Carga una imagen Docker local al cluster. |

En PowerShell (Windows), el equivalente de `eval $(minikube docker-env)` es:

```powershell
minikube docker-env | Invoke-Expression
```
