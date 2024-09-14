# ChatBot de Sir Isaac Newton

>[!NOTE]
> La estructura de interacción textual se basa en la plantilla proporcionada por [binary-hood](https://github.com/binary-hood/ChatBot-Starter).

En este fascinante proyecto, presentamos una aplicación de chat donde el venerado físico, matemático y astrónomo Sir Isaac Newton se convierte en el interlocutor principal. La aplicación permite a los usuarios entablar conversaciones en tiempo real con un personaje que encarna la profundidad y el rigor de Newton.

El sistema integra un backend en Python con un frontend en HTML y CSS, garantizando una experiencia de usuario tanto fluida como visualmente cautivadora.

## Estructura del Proyecto

El software se organiza en las siguientes secciones:

- **main/**: El directorio principal que contiene los componentes esenciales del proyecto.
  - **static/**: Almacena recursos estáticos como hojas de estilo CSS.
    - `style.css`: Archivo de estilos para la interfaz de usuario.
  - **templates/**: Contiene las plantillas HTML utilizadas por la aplicación.
    - `chat.html`: Plantilla principal para la experiencia de chat.
  - **.env**: Archivo de configuración para variables de entorno.
  - **.gitignore**: Define los archivos y directorios que Git debe omitir.
  - `app.py`: El archivo central que ejecuta la aplicación.
  - `prompt.py`: Archivo que gestiona las interacciones y respuestas del chatbot.
  - `README.md`: Este archivo, que proporciona información sobre el proyecto.
  - `requirements.txt`: Lista de dependencias necesarias para ejecutar la aplicación.

## Funcionalidades Principales

- **app.py**
  - Inicia el servidor web y gestiona las rutas de la aplicación.
  - Configura la conexión a la base de datos (si corresponde) y maneja las solicitudes de los usuarios.

- **prompt.py**
  - Contiene la lógica para procesar los mensajes de los usuarios y generar respuestas.
  - Utiliza una plantilla de prompt diseñada para capturar la esencia de Sir Isaac Newton.

```python
from langchain.prompts import PromptTemplate

issac_newton_template = """Eres Isaac Newton, el destacado físico, matemático y astrónomo del siglo XVII y XVIII. 
Tu conocimiento abarca una amplia gama de disciplinas científicas y matemáticas. 
Eres conocido por tu meticulosidad y tu profunda curiosidad por el mundo natural. 
Tu personalidad refleja una combinación de rigor académico y un entusiasmo contagioso por el descubrimiento y la comprensión.

**Instrucciones de Personalidad:**

1. **Tono Formal y Preciso:** Utiliza un lenguaje formal y preciso, reflejando el estilo académico de la época. Asegúrate de explicar conceptos complejos de manera clara y detallada.

2. **Curiosidad Intelectual:** Muestra un profundo interés en cuestiones científicas y matemáticas. No dudes en hacer preguntas adicionales para explorar a fondo los temas que se te presenten.

3. **Referencias Históricas y Científicas:** Utiliza ejemplos históricos y científicos relevantes para ilustrar tus puntos. Menciona tus propias teorías y descubrimientos, como la ley de la gravitación universal o el cálculo infinitesimal, cuando sea apropiado.

4. **Modestia Intelectual:** Aunque eres un experto en tu campo, muestra humildad y disposición a considerar nuevas ideas y descubrimientos. Reconoce los avances posteriores a tu época y cómo han contribuido al conocimiento actual.

5. **Interés en la Filosofía Natural:** Muestra un interés por la filosofía natural, es decir, la ciencia de la naturaleza en su totalidad, y discute cómo los principios científicos se relacionan con la comprensión más amplia del universo.

Historial de chat: {chat_history}
Pregunta: {question}
"""

isaac_newton_prompt = PromptTemplate(
    input_variables=["chat_history", "question"],
    template=issac_newton_template
)
```

- **style.css**
  - Define el diseño y la presentación de la interfaz de usuario.
  - Asegura que la aplicación sea visualmente atractiva y cómoda para el usuario.

- **chat.html**
  - Estructura la interfaz del chat.
  - Incluye elementos interactivos para enviar y recibir mensajes.

## Guía de Instalación

Para poner en marcha esta aplicación y entablar una conversación con el ilustre Newton, siga estos pasos:

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/gespitia/Isaac_Newton.git
   cd Isaac_Newton
   ```
2. Crear un entorno virtual (opcional, pero recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Linux/Mac
   venv\Scripts\activate  # En Windows
   ```
3. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Configurar las variables de entorno:
   - Crea un archivo `.env` en el directorio raíz y añade la siguiente variable:
     ```plaintext
     OPENAI_API_KEY="tu_open_ai_api_key"
     ```
5. Ejecutar la aplicación:
   ```bash
   python app.py
   ```

### Ejemplos de Uso

Una vez que la aplicación esté en funcionamiento, abre tu navegador y dirígete a `http://localhost:5000` para acceder a la interfaz de chat. Puedes empezar a enviar mensajes y recibir respuestas en tiempo real, todas inspiradas por el genio de Sir Isaac Newton.