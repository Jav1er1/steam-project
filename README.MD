# Steam Analytics App — Solución Profesional de Monitoreo de Cuenta Steam

## Descripción General

Steam Analytics App es una solución desarrollada en Python que consume la API oficial de Steam para obtener, procesar y visualizar estadísticas relevantes de una cuenta Steam en tiempo real.

La aplicación fue diseñada siguiendo un enfoque profesional orientado a automatización, seguridad y despliegue mediante Docker y Jenkins, integrando además buenas prácticas de desarrollo moderno como:

- Variables de entorno
- Control de versiones con GitHub
- Contenerización con Docker
- Automatización CI/CD con Jenkins
- Manejo robusto de errores
- Separación de dependencias
- Evidencias de ejecución

El sistema realiza consultas puntuales a la API de Steam y entrega información procesada directamente por consola, sin necesidad de mantener un servidor web en ejecución continua.

---

# Stakeholder

El principal stakeholder de esta solución es un jugador competitivo o usuario frecuente de Steam que necesita revisar rápidamente información relevante de su cuenta sin navegar manualmente por múltiples secciones de la plataforma Steam.

También puede ser utilizado por:

- Analistas de comportamiento gaming
- Streamers
- Jugadores competitivos
- Administradores de comunidades gaming
- Usuarios que desean monitorear estadísticas de juego

---

# Problema Detectado

Steam entrega una gran cantidad de información distribuida en distintas secciones de la plataforma, dificultando obtener una visión rápida y resumida del estado general de una cuenta.

Entre los principales problemas detectados:

- Estadísticas dispersas
- Dificultad para visualizar tiempo total de juego
- Poca centralización de información
- Necesidad de múltiples clics para acceder a datos relevantes
- Falta de automatización para análisis rápido

---

# Solución Implementada

La aplicación consume la API oficial de Steam y procesa automáticamente la información más relevante de una cuenta específica.

El sistema obtiene y muestra:

- Nombre del usuario
- Nivel de Steam
- Cantidad total de juegos
- Horas totales jugadas
- Top 5 juegos más utilizados
- Información del perfil

Toda la información es procesada mediante Python y presentada de forma clara por consola.

---

# Tecnologías Utilizadas

## Lenguajes y Librerías

- Python 3
- Requests

## Herramientas DevOps

- Docker
- Jenkins
- GitHub

## API Utilizada

- Steam Web API

---

# Arquitectura del Proyecto

```text
Usuario
   ↓
Python App
   ↓
Steam API
   ↓
Procesamiento de Datos
   ↓
Docker
   ↓
Jenkins Pipeline
   ↓
Automatización CI/CD
```

---

# Seguridad Implementada

Uno de los principales enfoques del proyecto fue evitar la exposición de credenciales sensibles.

Por esta razón:

- No se utilizaron API Keys hardcodeadas
- Se implementó uso de variables de entorno mediante la librería os
- Se configuró archivo .gitignore para evitar filtraciones accidentales

Ejemplo:

```python
API_KEY = os.getenv("STEAM_API_KEY")
```

---

# Manejo de Errores

La aplicación implementa manejo robusto de errores para garantizar estabilidad durante la ejecución.

Errores manejados:

- Error 401 → API Key inválida
- Error 404 → Recurso no encontrado
- Error 500 → Error interno servidor
- Timeout de conexión
- Error de conexión a Internet
- Respuesta JSON inválida
- Perfil privado o inexistente

---

# Estructura del Proyecto

```text
steam-project/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── build.sh
├── .gitignore
├── README.md
│
├── evidencias/
│   ├── docker/
│   │   ├── output.txt
│   │   └── screenshot.png
│   │
│   └── jenkins/
│       ├── stage_view.png
│       ├── console_output_build.png
│       ├── credentials.png
│       └── pipeline_script.txt
```

---

# Variables de Entorno

La aplicación requiere dos variables de entorno:

| Variable | Descripción |
|---|---|
| STEAM_API_KEY | API Key oficial de Steam |
| STEAM_ID | ID de usuario Steam |

---

# Configuración Variables de Entorno

## Linux / DEVASC

```bash
export STEAM_API_KEY="TU_API_KEY"
export STEAM_ID="76561198315513703"
```

## Windows PowerShell

```powershell
$env:STEAM_API_KEY="TU_API_KEY"
$env:STEAM_ID="76561198315513703"
```

---

# Instalación de Dependencias

```bash
pip3 install -r requirements.txt
```

---

# Ejecución Manual

```bash
python3 app.py
```

---

# Docker

## Construcción de Imagen

```bash
docker build -t steamapp .
```

## Ejecución del Contenedor

```bash
docker run --name samplerunning \
-e STEAM_API_KEY=$STEAM_API_KEY \
-e STEAM_ID=$STEAM_ID \
steamapp
```

---

# Automatización build.sh

El proyecto incluye un script de automatización encargado de:

- Construir imagen Docker
- Eliminar contenedores previos
- Ejecutar contenedor
- Mostrar estado Docker

Ejecución:

```bash
chmod +x build.sh
./build.sh
```

---

# Jenkins CI/CD

El proyecto implementa integración continua mediante Jenkins utilizando:

## BuildAppJob

Trabajo Freestyle encargado de:

- Clonar repositorio GitHub
- Ejecutar script build.sh
- Construir imagen Docker
- Ejecutar contenedor

## SamplePipeline

Pipeline encargado de orquestar el flujo completo en dos etapas:

### Preparation

- Detiene contenedor previo
- Elimina contenedor anterior
- Continúa aunque no exista contenedor

### Build

- Ejecuta BuildAppJob
- Construye imagen
- Corre contenedor
- Obtiene datos reales API

---

# Pipeline Script Utilizado

```groovy
node {

 stage('Preparation') {

  catchError(buildResult: 'SUCCESS') {

   sh 'docker stop samplerunning'
   sh 'docker rm samplerunning'

  }
 }

 stage('Build') {

  build 'BuildAppJob'

 }

}
```

---

# Evidencias Incluidas

## Docker

- output.txt
- screenshot.png

## Jenkins

- stage_view.png
- console_output_build.png
- credentials.png
- pipeline_script.txt

---

# Flujo Completo del Proyecto

```text
GitHub
   ↓
Jenkins
   ↓
Pipeline
   ↓
Docker Build
   ↓
Docker Run
   ↓
Steam API
   ↓
Procesamiento Python
```

---

# Resultado Esperado

La aplicación entrega información procesada similar a:

```text
🔄 Obteniendo datos Steam...

👤 PERFIL

Nombre: Usuario
Nivel Steam: 25
Cantidad Juegos: 120

🔥 TOP 5 JUEGOS
- Counter Strike 2
- GTA V
- Rust
- PUBG
- Apex Legends
```

---

# Conclusión

Steam Analytics App demuestra la integración completa entre desarrollo de software, automatización y contenerización, aplicando buenas prácticas de seguridad y despliegue profesional.

El proyecto permite automatizar el análisis de cuentas Steam mediante una solución reproducible, portable y escalable, integrando Python, Docker, GitHub y Jenkins dentro de un flujo CI/CD completamente funcional.
