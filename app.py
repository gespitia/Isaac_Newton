from flask import Flask, render_template, request, jsonify
from langchain import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI
from prompt import isaac_newton_prompt
import os
from dotenv import load_dotenv

# Carga las variables de entorno del archivo .env
load_dotenv()  
api_key = os.getenv('OPENAI_API_KEY')  # Obtiene la clave de la variable de entorno

# Inicializa el modelo de OpenAI (actualmente se esta usando gpt-4o-mini)
modelo = 'gpt-4o-mini'
llm = ChatOpenAI(model=modelo, temperature=0.1)

# Configura la memoria para el historial de la conversación
conversation_memory = ConversationBufferMemory(
    memory_key="chat_history",
    max_len=200,
    return_messages=True
)

# Configura la cadena de LangChain con el modelo de lenguaje y el prompt
llm_chain = LLMChain(llm=llm, prompt=isaac_newton_prompt, memory=conversation_memory)

app = Flask(__name__)

# Página principal
@app.route("/")
def index():
    return render_template("chat.html")

# Respuesta del chatbot
@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    return get_chat_response(msg)

# Función para obtener la respuesta del chat
def get_chat_response(user_input):
    # Procesa la entrada del usuario y genera la respuesta usando LangChain
    response = llm_chain.run({"question": user_input})
    return response

if __name__ == '__main__':
    app.run()