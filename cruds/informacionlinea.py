from models.informacion import OBJCategoria
from google import genai
from google.genai import types
import re
from collections import deque
import os

def asistentechatbot(mensaje_usuario: str,evento: int) -> str:
    """
    Función principal que procesa el mensaje del usuario y devuelve una respuesta.
    No mantiene estado entre llamadas (sin memoria).
    """
    try:
        # Normalizar el texto (conversión rápida a minúsculas)
        mensaje_limpio = mensaje_usuario.lower().strip()
        
        # Para todo lo demás, dejamos que la IA interprete y genere la respuesta
        return generar_respuesta_ia(mensaje_limpio,evento)
            
    except Exception as e:
        # Manejo de errores simplificado
        return "",

#curva peligrosa, zona de derrumbe,  zona escolar
def generar_respuesta_ia(mensaje_limpio: str,evento: int) -> str:
    """
    Utiliza la IA para interpretar y generar una respuesta apropiada"""

    try:

        # Crear el cliente del nuevo SDK
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

        #Saludo
        if evento==1:
            prompt = f"""
            Actúa como el asistente de conducción de LineaAI.

            Contexto:
            La aplicación está lista para iniciar el viaje y el conductor comenzará su recorrido.
            {mensaje_limpio}

            Instrucciones:
            - Genera un mensaje breve de bienvenida para iniciar el recorrido.
            - Usa un tono moderno, amigable y natural, como el de una app de navegación.
            - El mensaje debe tener exactamente 2 oraciones en un solo párrafo.
            - No enumeres ni uses formato de lista.
            - No uses términos técnicos.
            - Mantén el mensaje claro, positivo y motivador.

            Responde únicamente con el mensaje final.
            """
         #- No menciones sistemas ni tecnología.
        #eventos 
        if evento==2:
            prompt = f"""
                    Actúa como un asistente profesional de conducción.

                    Contexto:
                    El vehículo se aproxima a los siguientes eventos viales:
                    {mensaje_limpio}

                    Genera una advertencia automática preventiva para el conductor.

                    Reglas obligatorias:
                    - Integra todos los eventos de forma natural en un párrafo coherente de 2 a 3 oraciones.
                    - No enumeres ni uses formato de lista.
                    - No menciones sistemas ni tecnología.
                    - No uses términos técnicos como "geocerca" o "tramo".
                    - No agregues información que no esté presente en los eventos.
                    - Mantén el mensaje breve, claro y agradable.
                    - Usa un tono moderno, amigable y natural, como una app moderna de navegación.
                    
                    La respuesta debe ser solo la frase final, sin explicaciones.
                    """
        #Salida
        if evento==3:
            prompt = f"""
            Actúa como el asistente de conducción de LineaAI.

            Contexto:
            El conductor está por finalizar su recorrido y la aplicación notificará el cierre del viaje.
            {mensaje_limpio}

            Instrucciones:
            - Genera un mensaje breve de finalización del recorrido.
            - Usa un tono moderno, amigable y natural, como el de una app de navegación.
            - El mensaje debe tener exactamente 2 oraciones en un solo párrafo.
            - No enumeres ni uses formato de lista.
            - No uses términos técnicos.
            - Mantén el mensaje claro, positivo y agradable.

            Responde únicamente con el mensaje final.
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


