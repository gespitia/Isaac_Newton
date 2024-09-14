# Don Quijote ChatBot


>[!NOTE]
> La plantilla de la interacción de texto fue extraida de [binary-hood](https://github.com/binary-hood/ChatBot-Starter)

Este proyecto es una aplicación de chat que permite a los usuarios interactuar en tiempo real. 
El personaje principal de este chat es Don Quijote de la Mancha, este personaje unico usara su particular experiencia y forma de hablar para responder a tus preguntas.

Utiliza un backend en Python y un frontend en HTML/CSS para ofrecer una experiencia de usuario fluida y atractiva.


## Arquitectura del Software

La arquitectura de la aplicación se compone de lo siguiente:

  - **main/**: Directorio principal que contiene los archivos esenciales del proyecto.
      - **static/**: Contiene archivos estáticos como hojas de estilo CSS.
         - `style.css`: Archivo de estilos para la interfaz de usuario.
      - **templates/**: Contiene las plantillas HTML utilizadas por la aplicación.
         - `chat.html`: Plantilla principal para la interfaz de chat.
      - **.env**: Archivo de configuración para variables de entorno.
      - **.gitignore**: Especifica los archivos y directorios que deben ser ignorados por Git.
      - `app.py`: Archivo principal que ejecuta la aplicación.
      - `prompt.py`: Archivo que gestiona las interacciones y las respuestas del chat.
      - `README.md`: Este archivo, que proporciona información sobre el proyecto.
      - `requirements.txt` Lista de dependencias necesarias para ejecutar la aplicación.
  


## Funciones Principales

- **app.py**
  - Inicia el servidor web y gestiona las rutas de la aplicación.
  - Configura la conexión a la base de datos (si aplica) y maneja las solicitudes de los usuarios.

- **prompt.py**
  - Contiene la lógica para procesar los mensajes de los usuarios y generar respuestas.
  - Utiliza un modelo de lenguaje para ofrecer respuestas coherentes y relevantes.

- **style.css**
  - Define el diseño y la presentación de la interfaz de usuario.
  - Asegura que la aplicación sea visualmente atractiva y fácil de usar.

- **chat.html**
  - Estructura la interfaz de usuario del chat.
  - Incluye elementos interactivos para enviar y recibir mensajes.


## Instrucciones de Instalación

Para instalar y ejecutar la aplicación, sigue estos pasos:

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Yessid-ML/Don_Quijote_chat.git
   cd Don_Quijote_chat
2. Crea un entorno virtual (opcional pero recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Linux/Mac
    venv\Scripts\activate  # En Windows
3. Instala dependencias
    ```bash
    pip install -r requirements.txt
4. Configura las variables de entorno
    ```bash
    .env file
    dentro del .env crea una la siguiente variable: OPENAI_API_KEY="tu open ai api key"
5. Ejecuta la aplicacion.
    ```bash
    python app.py
### Ejemplos de Uso
```markdown
## Ejemplos de Uso

Una vez que la aplicación esté en funcionamiento, abre tu navegador y dirígete a `http://localhost:5000` para acceder a la interfaz de chat. Puedes empezar a enviar mensajes y recibir respuestas en tiempo real.
