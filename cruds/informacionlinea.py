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
        Actúa como Linea IA, un asistente avanzado de conducción predictiva.

        Contexto:
        El vehículo se aproxima a los siguientes eventos dentro de una geocerca:
        {eventos}

        Tu función:
        Generar una advertencia automática preventiva para el conductor.

        Lineamientos profesionales:
        - No hagas preguntas.
        - No enumeres los eventos como lista.
        - Integra todos los eventos en un solo mensaje fluido.
        - Prioriza la seguridad y el riesgo implícito.
        - Usa lenguaje natural, técnico pero cercano.
        - Transmite anticipación, no alarma exagerada.
        - Sé claro, firme y breve.

        El mensaje debe sonar como un sistema de navegación inteligente de alto nivel.
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


