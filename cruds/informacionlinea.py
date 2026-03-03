from models.informacion import OBJCategoria
from google import genai
from google.genai import types
import re
from collections import deque
import os

def asistentechatbot(mensaje_usuario: str) -> str:
    """
    Función principal que procesa el mensaje del usuario y devuelve una respuesta.
    No mantiene estado entre llamadas (sin memoria).
    """
    try:
        # Normalizar el texto (conversión rápida a minúsculas)
        mensaje_limpio = mensaje_usuario.lower().strip()
        
        # Para todo lo demás, dejamos que la IA interprete y genere la respuesta
        return generar_respuesta_ia(mensaje_limpio)
            
    except Exception as e:
        # Manejo de errores simplificado
        return "",

#curva peligrosa, zona de derrumbe,  zona escolar
def generar_respuesta_ia(eventos: str) -> str:
    """
    Utiliza la IA para interpretar y generar una respuesta apropiada"""

    try:

        # Crear el cliente del nuevo SDK
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


        # Prompt completo con contexto de la lista de eventos
        prompt = f"""
                Actúa como un asistente profesional de conducción.

                Contexto:
                El vehículo se aproxima a los siguientes eventos viales:
                {eventos}

                Genera una advertencia automática preventiva para el conductor.

                Reglas obligatorias:
                - Integra todos los eventos de forma natural dentro de una sola frase.
                - No enumeres ni uses formato de lista.
                - No menciones sistemas ni tecnología.
                - No uses términos técnicos como "geocerca" o "tramo".
                - No agregues información que no esté presente en los eventos.
                - Mantén el mensaje breve, claro y agradable.
                - Usa un tono moderno, amigable y natural, como una app moderna de navegación.
                
                La respuesta debe ser solo la frase final, sin explicaciones.
                """
        # Llamada correcta al nuevo modelo
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(temperature=0.7,top_p=0.95,top_k=40)
        )

        texto = response.text  # ✔ forma correcta de leer el texto

        if texto:
            return texto.strip()
        else:
            return ""
    except Exception as e:
            return ""


