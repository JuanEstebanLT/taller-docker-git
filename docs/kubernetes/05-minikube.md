# 2. Minikube

## 2.1 ¿Qué es Minikube?

**Minikube** ejecuta un cluster Kubernetes de **un solo nodo** en tu máquina. Sirve para aprender, desarrollar y probar sin pagar un cluster en la nube.

Por debajo usa un driver (Docker, Hyper-V, VirtualBox, etc.) para levantar la máquina o el contenedor donde corre Kubernetes.

## 2.2 Requisitos habituales

- Docker (recomendado como driver) o un hipervisor (Hyper-V / VirtualBox).
- `kubectl` instalado (Minikube puede instalarlo también).
- CPU y RAM suficientes: un mínimo razonable es 2 CPU y 2 GB; para pruebas más cómodas, 4 CPU y 8 GB.

## 2.3 Instalación (Windows)

1. Instalar [Docker Desktop](https://www.docker.com/products/docker-desktop/) o habilitar Hyper-V.
2. Instalar Minikube desde la [documentación oficial](https://minikube.sigs.k8s.io/docs/start/).
3. Instalar `kubectl` (incluido con Docker Desktop, o vía el instalador de Kubernetes).

Comprobar:

```bash
minikube version
kubectl version --client
```

## 2.4 ¿Por qué usar Minikube?

- **Aprendizaje:** entender Kubernetes sin costos de nube.
- **Desarrollo:** probar aplicaciones en local antes de desplegar.
- **Experimentación:** probar configuraciones, add-ons y funcionalidades.
- **Portabilidad:** el cluster local se comporta como uno de producción (API, recursos y YAML iguales).

## 2.5 Primer arranque

```bash
minikube start --driver=docker
minikube status
kubectl get nodes
```

En Windows, si Docker no está disponible:

```bash
minikube start --driver=hyperv
```

Asignar recursos:

```bash
minikube start --driver=docker --cpus=4 --memory=8192
```

La referencia completa de comandos está en [`08-referencia-minikube.md`](08-referencia-minikube.md).
