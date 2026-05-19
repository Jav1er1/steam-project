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

- Buscar Juegos en la biblioteca del usuario
- Ver los top juegos globales jugados por los usuarios
- Visualizar el perfil del usuario
- Visualizar los juegos mas jugados por el usuario
- Buscar a otros usuarios
- Comparar informacion de Juegos/horas con demás usuarios

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
├── Dockerfile
├── requirements.txt
├── README.md
├── output.txt
├── Jenkinsfile
│
├── evidencias/
│   ├── docker_funcionando.png
│   ├── github_final.png
│   ├── jenkins_success.png
│   ├── pipeline_success.png
│   └── stage_view.png
│
└── __pycache__/
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
export STEAM_API_KEY="CED9B4D212D63B7C80CA497368C4801B"
export STEAM_ID="76561198315513703"
```

## Windows PowerShell

```powershell
$env:STEAM_API_KEY="CED9B4D212D63B7C80CA497368C4801B"
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

- docker_funcionando.png

## Jenkins

- stage_view.png
- console_output_build.png
- pipeline_script.png
- pipeline_script.txt
- github_config.png

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
================================
       STEAM MANAGER PRO
================================
1. Buscar juegos de mi biblioteca
2. Ver top juegos globales
3. Ver mi perfil
4. Ver mis juegos más jugados
5. Buscar usuario Steam
6. Comparar perfiles
7. Salir
================================

Seleccione una opción: 1
[H[2J[3J================================
    BUSCAR JUEGO EN MI CUENTA
================================

Ingrese nombre del juego: Rust

🔄 Buscando en tu biblioteca...

🎮 Rust
⏰ Horas jugadas: 1286.5
🆔 APP ID: 252490
--------------------------------
🎮 Rust - Staging Branch
⏰ Horas jugadas: 0.0
🆔 APP ID: 700580
--------------------------------

Presione ENTER para continuar...
[H[2J[3J================================
       STEAM MANAGER PRO
================================
1. Buscar juegos de mi biblioteca
2. Ver top juegos globales
3. Ver mi perfil
4. Ver mis juegos más jugados
5. Buscar usuario Steam
6. Comparar perfiles
7. Salir
================================

Seleccione una opción: 1
[H[2J[3J================================
    BUSCAR JUEGO EN MI CUENTA
================================

Ingrese nombre del juego: Unturned

🔄 Buscando en tu biblioteca...

🎮 Unturned
⏰ Horas jugadas: 3448.6
🆔 APP ID: 304930
--------------------------------

Presione ENTER para continuar...
[H[2J[3J================================
       STEAM MANAGER PRO
================================
1. Buscar juegos de mi biblioteca
2. Ver top juegos globales
3. Ver mi perfil
4. Ver mis juegos más jugados
5. Buscar usuario Steam
6. Comparar perfiles
7. Salir
================================

Seleccione una opción: 3
[H[2J[3J================================
           MI PERFIL
================================

🎮 Nombre: Skyland ツ
🌐 Perfil: https://steamcommunity.com/id/Sk1_LaND/
🖼️ Avatar: https://avatars.steamstatic.com/db5a334116ea8b5fff0e3288eb07a895485bbb14_full.jpg
🟢 Estado: Online

Presione ENTER para continuar...
[H[2J[3J================================
       STEAM MANAGER PRO
================================
1. Buscar juegos de mi biblioteca
2. Ver top juegos globales
3. Ver mi perfil
4. Ver mis juegos más jugados
5. Buscar usuario Steam
6. Comparar perfiles
7. Salir
================================

Seleccione una opción: 4
[H[2J[3J================================
       MIS JUEGOS TOP
================================

🎮 Counter-Strike 2
⏰ Horas jugadas: 3740.8
--------------------------------
🎮 Unturned
⏰ Horas jugadas: 3448.6
--------------------------------
🎮 Rust
⏰ Horas jugadas: 1286.5
--------------------------------
🎮 Terraria
⏰ Horas jugadas: 90.7
--------------------------------
🎮 7 Days to Die
⏰ Horas jugadas: 81.4
--------------------------------
🎮 Among Us
⏰ Horas jugadas: 52.0
--------------------------------
🎮 Team Fortress 2
⏰ Horas jugadas: 39.1
--------------------------------
🎮 Geometry Dash
⏰ Horas jugadas: 36.5
--------------------------------
🎮 Fall Guys
⏰ Horas jugadas: 32.1
--------------------------------
🎮 Overcooked! 2
⏰ Horas jugadas: 26.5
--------------------------------

Presione ENTER para continuar...
[H[2J[3J================================
       STEAM MANAGER PRO
================================
1. Buscar juegos de mi biblioteca
2. Ver top juegos globales
3. Ver mi perfil
4. Ver mis juegos más jugados
5. Buscar usuario Steam
6. Comparar perfiles
7. Salir
================================

Seleccione una opción: 5
[H[2J[3J================================
        BUSCAR USUARIO
================================

Ingrese SteamID64: 76561198149320254

🎮 Nombre: Sabroson
🌐 Perfil: https://steamcommunity.com/id/Sidoryney/
🖼️ Avatar: https://avatars.steamstatic.com/43429fb206a3ce01a5ee3c3de08d6ebdaddf8b43_full.jpg

Presione ENTER para continuar...
[H[2J[3J================================
       STEAM MANAGER PRO
================================
1. Buscar juegos de mi biblioteca
2. Ver top juegos globales
3. Ver mi perfil
4. Ver mis juegos más jugados
5. Buscar usuario Steam
6. Comparar perfiles
7. Salir
================================

Seleccione una opción: 6
[H[2J[3J================================
       COMPARAR PERFILES
================================

Ingrese SteamID64 a comparar: 76561198149320254

========== RESULTADOS ==========

🎮 Tus juegos: 40
🎮 Juegos otro usuario: 43

⏰ Tus horas: 9015.2
⏰ Horas otro usuario: 2775.4

🤝 Juegos en común: 17
🎮 Team Fortress 2
🎮 Left 4 Dead 2
🎮 Portal 2
🎮 Counter-Strike 2
🎮 Borderlands 2
🎮 PAYDAY 2
🎮 The Forest
🎮 Rust
🎮 Unturned
🎮 Dead Island Riptide Definitive Edition

Presione ENTER para continuar...
[H[2J[3J================================
       STEAM MANAGER PRO
================================
1. Buscar juegos de mi biblioteca
2. Ver top juegos globales
3. Ver mi perfil
4. Ver mis juegos más jugados
5. Buscar usuario Steam
6. Comparar perfiles
7. Salir
================================

Seleccione una opción: 7

👋 Cerrando aplicación...
```

---

# Conclusión

Steam Analytics App demuestra la integración completa entre desarrollo de software, automatización y contenerización, aplicando buenas prácticas de seguridad y despliegue profesional.

El proyecto permite automatizar el análisis de cuentas Steam mediante una solución reproducible, portable y escalable, integrando Python, Docker, GitHub y Jenkins dentro de un flujo CI/CD completamente funcional.
