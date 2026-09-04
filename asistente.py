import os
from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()  # Load environment variables from .env file

API_KEY = os.getenv("GENAI_API_KEY")

# Inicializar el cliente
client = genai.Client(api_key=API_KEY)

configuration = types.GenerateContentConfig(
    max_output_tokens=2048,
    temperature=0,
    system_instruction="""Asistente Legal/Normativo de la Universidad Konrad Lorenz: basado en reglamentos o contratos. 

Tus respuestas deben ser concisas, seguras, basados en los normas y regulaciones de la universidad, teniendo presente que el usuario es un estudiante o miembro de la comunidad universitaria.
Al responder sobre alguna norma o contrato, debes proporcionar información precisa y relevante. Siemore en base a las normas de la universidad.
Si te hacen una pregunta que no está realicionada con con las normativas de la universidad, responde 'Lo siento, solo puedo responder preguntas sobre la normativa de la universidad'. """
)

MODEL = "gemini-3.5-flash-lite"

# Historial para simular la memoria del agente durante esta ejecución.
conversation_history = [
    {
        "role": "user",
        "parts": [{"text": "¿Cuanto es la cantidad minima de inasistencias para perder una asignatura por fallas en la Universidad Konrad Lorenz?"}]
    },
    {
        "role": "model",
        "parts": [{"text": "Según el reglamento académico de la Universidad Konrad Lorenz, un estudiante puede perder una asignatura por inasistencias si acumula más del 20% de inasistencias en el total de clases programadas para esa asignatura. Es importante que los estudiantes revisen el reglamento específico de su programa académico para obtener información detallada."}]
    },
    {
        "role": "user",
        "parts": [{"text": "¿mi asignatura tiene una intensidad de 4 horas a la semana ?"}]
    },
    {
        "role": "model",
        "parts": [{"text": "Si tu materia tiene una intensidad de 4 horas a la semana, solo puedes fallar un maximo de 12 horas."}]
    }
]

print("-- Asistente Legal/Normativo  --")
print("(Escribe 'salir' para terminar)\n")

while True:
        user_input = input("Usuario: ")
        
        if user_input.lower() in ["salir", "exit", "quit"]:
            print("Asistente: ¡Hasta pronto! Sigue practicando.")
            break

        try:
            conversation_history.append({
                "role": "user",
                "parts": [{"text": user_input}]
            })

            response = client.models.generate_content(
                model=MODEL,
                contents=conversation_history,
                config=configuration
            )
            
            assistant_message = response.text
            conversation_history.append({
                "role": "model",
                "parts": [{"text": assistant_message}]
            })

            print(f"\nAsistente: {assistant_message}\n")

        except Exception as e:            
            print(f"Error al procesar la solicitud: {e}")

