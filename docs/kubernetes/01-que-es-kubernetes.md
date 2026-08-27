# 1. ¿Qué es Kubernetes?

## 1.1 Definición

**Kubernetes** (también conocido como **K8s**, donde “8” representa las 8 letras entre la “K” y la “s” de Kubernetes) es una plataforma de **orquestación de contenedores de código abierto**, diseñada para automatizar el despliegue, el escalado y la gestión de aplicaciones contenedorizadas.

Fue originalmente desarrollado por **Google** (basado en su sistema interno llamado **Borg**) y posteriormente donado a la **Cloud Native Computing Foundation (CNCF)** en 2015. Hoy en día es el estándar de facto para la orquestación de contenedores en la industria.

## 1.2 ¿Por qué necesitamos Kubernetes?

Antes de Kubernetes, las aplicaciones se ejecutaban directamente en servidores físicos o máquinas virtuales. Con la llegada de los contenedores (especialmente Docker), surgió un nuevo problema: **¿cómo gestionar cientos o miles de contenedores de forma eficiente?**

Kubernetes resuelve ese problema automatizando tareas que, hechas a mano, no escalan:

- **Despliegue** de contenedores en varios nodos.
- **Escalado** (más o menos réplicas según la demanda).
- **Autoreparación**: si un contenedor o un nodo falla, se recrean los Pods.
- **Descubrimiento de servicios** y balanceo de carga.
- **Actualizaciones** sin downtime (rolling updates) y **rollback**.
- **Gestión de configuración y secretos**.
- **Almacenamiento persistente** para aplicaciones con estado.

Docker crea y ejecuta contenedores. Kubernetes decide **dónde** corren, **cuántos** hay, **cómo** se exponen en red y **qué hacer** cuando algo falla.
