from models.informacion import OBJCategoria
import google.generativeai as genai
import re
from collections import deque
import os
# Configuración de la API de Google Generative AI   AIzaSyCmjRN_xL07aRkftfoUba3nHW-_hkrZwnc
#AIzaSyAQ60ndktxOiAopNpE_CHYxV6QSs2-oyxs
API_KEY = os.getenv("TOKEN_GEMINI")  
genai.configure(api_key=API_KEY)
  
 
 
# Solo mantenemos el patrón de saludos para respuesta rápida
PATRON_SALUDO = re.compile(r'\b(hola|hl|mano|hi|hey|buenos dias|que tal|buenas|buenas tardes|buenas noches|saludos)\b')
RESPUESTA_SALUDO = "¡Hola! ¿En qué puedo ayudarte hoy?"
RESPUESTA_ERROR = "Ups... algo salió mal al procesar tu mensaje 😓. ¿Podrías intentarlo otra vez, por favor?"


def asistentechatbot2(mensaje_usuario: str) -> str:
    """
    Función principal que procesa el mensaje del usuario y devuelve una respuesta.
    No mantiene estado entre llamadas (sin memoria).
    """
    try:
        # Normalizar el texto (conversión rápida a minúsculas)
        mensaje_limpio = mensaje_usuario.lower().strip()
        
        # Solo verificamos si es un saludo con respuesta rápida
        if PATRON_SALUDO.search(mensaje_limpio):
            return RESPUESTA_SALUDO
        
        # Para todo lo demás, dejamos que la IA interprete y genere la respuesta
        return generar_respuesta_ia(mensaje_usuario)
            
    except Exception as e:
        # Manejo de errores simplificado
        return RESPUESTA_ERROR

def generar_respuesta_ia(consulta: str) -> str:
    """
    Utiliza la IA para interpretar y generar una respuesta apropiada,
    ya sea sobre la radio o sobre cualquier otro tema.
    """

    try:
        # Configuración para Gemini
        model = genai.GenerativeModel(
            'gemini-2.0-flash',
            generation_config={
                "temperature": 0.8,
                "top_p": 0.95,
                "top_k": 40
            }
        )

        
        # Prompt completo con contexto de la radio
        prompt = f"""
        Actúa como *TripleG AI*, el asistente virtual de canchas deportivas. Responde la siguiente consulta con un tono **amigable, claro y profesional**:

        "{consulta}"

        Sigue estas instrucciones al generar tu respuesta:

        🔸 **Horarios de alquiler:**
        - **Día:** de 8:00 a. m. a 6:00 p. m.
        - **Noche:** de 6:00 p. m. a 11:00 p. m.
        - **Día completo:** de 8:00 a. m. a 11:00 p. m.

        🔸 **Precios por hora:**
        - **Día:** S/ 50.00 por hora.
        - **Noche:** S/ 70.00 por hora.

        🔸 **Disponibilidad:**
        - Solo cuentas con **2 canchas deportivas**: *Cancha 1* y *Cancha 2*.

        🔸 **Instrucciones para cotizar:**
        - Si el usuario quiere alquilar por horas, calcula el total multiplicando las horas solicitadas por el precio correspondiente (día o noche).
        - Si el usuario quiere alquilar por *todo el día* o *día completo*, realiza el siguiente cálculo:
        - Total sin descuento = (número de horas diurnas × S/ 50.00) + (número de horas nocturnas × S/ 70.00)
        - También muestra:
            - Total con 5% de descuento
            - Total con 10% de descuento

        🔸 **Ejemplo de formato esperado para una cotización por día completo:**
        - Total sin descuento: S/ XXX.XX
        - Total con 5% de descuento: S/ XXX.XX
        - Total con 10% de descuento: S/ XXX.XX

        Responde siempre con claridad y amabilidad, como si estuvieras ayudando a un cliente en persona.
        """
        response = model.generate_content(prompt)
        if response.text:
            return response.text.strip()
        else:
            return "Lo siento, no puedo responder a esa consulta en este momento"
    except Exception as e:
            return "Disculpa, no pude generar una respuesta"


