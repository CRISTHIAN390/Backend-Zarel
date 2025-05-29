from models.informacion import OBJCategoria
from collections import deque
import google.generativeai as genai
import re
from datetime import datetime
def obtener_informacion(categoria: str):
    base_url_mundo = "https://backend-zarel.onrender.com/static/img/noticias/mundo/"
    base_url_peru = "https://backend-zarel.onrender.com/static/img/noticias/peru/"
    datos = {
        "Mundo": [
            OBJCategoria(
                id=1,
                titulo="Llamada Putin a Trump deja a la EEUU en el limbo sobre la guerra en Ucrania",
                url=base_url_mundo + "noticia2.png",
                fecha="2025-05-19",
                hora="13:05",
                descripcion = """
                <ul>
                <li><b>Putin y Trump discutieron un posible memorando de paz, pero Rusia sigue imponiendo condiciones difíciles y mantiene su ofensiva militar.</b></li>
                <li><b>La Unión Europea y Ucrania esperaban un alto el fuego inmediato, pero solo se logró un posible "preludio" sin compromisos concretos.</b></li>
                <li><b>Rusia continúa con ataques y refuerzos militares, lo que contradice su aparente interés en una solución pacífica.</b></li>
                </ul>
                <p>
                  La llamada entre Putin y Trump ha generado expectativas sobre un posible memorando de entendimiento que sirva como antesala a un acuerdo de paz entre Rusia y Ucrania. Aunque ambos líderes calificaron el diálogo como positivo, las condiciones planteadas por Putin —como que Ucrania ceda territorio y renuncie a entrar en la OTAN— reflejan una propuesta difícil de aceptar para Kiev y sus aliados.
                </p>
                <div class="detalle-noticia-image-container-123">
                    <img src="https://backend-zarel.onrender.com/static/img/noticias/mundo/noticia1.png" alt="Imagen relacionada" class="detalle-noticia-image-content-123" />
                </div> 
               <p>
                A pesar del tono diplomático, Rusia mantiene una ofensiva activa en Ucrania y ha intensificado su presencia militar en regiones cercanas a Europa. Esto, sumado al escepticismo de la UE y las declaraciones de antiguos diplomáticos estadounidenses, pone en duda que las negociaciones actuales representen un verdadero avance hacia una paz duradera.
                </p>
                """.strip(),
                estado=True
            ),
            OBJCategoria(
                id=2,
                titulo="EE.UU. y China acuerdan reducir aranceles por 90 días: impacto y riesgos para la economía mundial y el Perú",
                url=base_url_mundo + "noticia4.png",
                fecha="2025-05-19",
                hora="13:40",
                descripcion = """
                <ul>
                <li><b>Estados Unidos y China acordaron reducir sus aranceles de manera significativa por 90 días.</b></li>
                <li><b>Las nuevas tasas bajan al 30% para productos chinos y al 10% para productos estadounidenses.</b></li>
                <li><b>Ambos países deben aplicar las medidas antes del 14 de mayo, según lo anunció la Casa Blanca.</b></li>
                </ul>
                <p>
                 Estados Unidos y China acordaron una reducción significativa de aranceles tras una reunión en Suiza. El acuerdo, con una duración de 90 días, busca aliviar tensiones comerciales y reactivar el intercambio entre ambas economías.
                </p>
                <div class="detalle-noticia-image-container-123">
                    <img src="https://backend-zarel.onrender.com/static/img/noticias/mundo/noticia3.png" alt="Imagen relacionada" class="detalle-noticia-image-content-123" />
                </div> 
               <p>
                    Aunque las reducciones son notables, el pacto es temporal y debe aplicarse antes del 14 de mayo. Su efectividad dependerá de la voluntad política y del impacto que tenga en las relaciones a largo plazo.
                </p>
                """.strip(),
                estado=True
            ),
            OBJCategoria(
                id=3,
                titulo='La potencia global que desafiará a EE. UU. y China en 2030: dos países de Latinoamérica podrían convertirse en las próximas “naciones prósperas”',
                url=base_url_mundo + "noticia6.png",
                fecha="2025-05-19",
                hora="14:30",
                descripcion = """
                <ul>
                <li><b>Brasil y México serán las dos naciones latinoamericanas en el Top 10 mundial según proyecciones de PwC para los próximos 5 años.</b></li>
                <li><b>Brasil ocupará el octavo lugar con un PIB estimado de $4.439 billones y México el noveno con $3.661 billones.</b></li>
                <li><b>India podría superar a Estados Unidos para 2050, mientras Indonesia avanzaría al cuarto lugar, reflejando cambios en la economía global.</b></li>
                </ul>
                <p>
                 La estabilidad monetaria es clave para el crecimiento económico y el desarrollo de un país, ya que facilita que este fortalezca sus capacidades año tras año. Según un informe de PwC proyectado hacia 2050, mientras Estados Unidos y China continúan liderando, una nueva potencia mundial podría desafiar su posición. Además, dos países latinoamericanos, Brasil y México, generan expectativas al proyectarse como futuras “naciones ricas” en los próximos cinco años, integrándose al Top 10 de las economías más importantes del mundo.
                </p>
                <div class="detalle-noticia-image-container-123">
                    <img src="https://backend-zarel.onrender.com/static/img/noticias/mundo/noticia5.png" alt="Imagen relacionada" class="detalle-noticia-image-content-123" />
                </div> 
               <p>
                    El informe destaca el Producto Interno Bruto (PIB) como indicador fundamental para estas proyecciones, estimando que Brasil ocupará el octavo lugar con un PIB de $4.439 billones y México el noveno con $3.661 billones. Además, se menciona que economías emergentes como India podrían superar a Estados Unidos para 2050, mientras otros países como Indonesia también escalarán posiciones, reflejando una transformación significativa en el orden económico global.
                </p>
                """.strip(),
                estado=True
            )
        ],
        "Peru": [
            OBJCategoria(
                id=1,
                titulo="Terror en el Jockey Plaza: Clientes fueron encerrados en tiendas mientras autoridades controlaban la emergencia",
                url=base_url_peru + "noticia2.png",
                fecha="2025-05-18",
                hora="09:15",
                descripcion = """
                <ul>
                <li><b>Los clientes se refugiaron en las diversas tiendas para ponerse a buen resguardo</b></li>
                <li><b>La Policía Nacional del Perú explicó lo sucedido</b></li>
                <li><b>Disparos en el primer piso del establecimiento</b></li>
                </ul>
                <p>
                  Minutos de pánico y terror se vivieron en el centro comercial
                  Jockey Plaza, ubicado en Santiago de Surco, debido 
                  a una supuesta balacera.
                  Ciudadanos se refugiaron en las tiendas del lugar para intentar salvaguardar sus vidas ante la emergencia.
                </p>
                <div class="detalle-noticia-image-container-123">
                    <img src="https://backend-zarel.onrender.com/static/img/noticias/peru/noticia1.png" alt="Imagen relacionada" class="detalle-noticia-image-content-123" />
                </div> 
               <p>
                Según testigos, se escucharon disparos en el primer piso del 
                establecimiento al promediar las 2 de la tarde de este domingo 
                18 de mayo.
                Tras los estruendos de aparentemente un arma de fuego, 
                los clientes corrieron despavoridos. Las autoridades 
                desplagaron el protocolo correspondiente para actuar según 
                lo ocurrido.
                </p>
                """.strip(),
                estado=True
            ),
            OBJCategoria(
                id=2,
                titulo='"Cuchillo" robó 200 toneladas de materal aurífero en Pataz valorizado en US$ 1.2 millones',
                url=base_url_peru + "noticia4.png",
                fecha="2025-05-19",
                hora="11:00",
                descripcion = """
                <ul>
                <li><b>Libmar SAC es una de las empresas de Segundo Cueva Rojas en Pataz</b></li>
                <li><b>Los 13 trabajadores asesinados resguardaban a la empresa Libmar de Segundo Cueva.</b></li>
                <li><b>Revelan nuevos audios que confirmarían complot de Fernández Jerí contra fiscales del equipo Lava Jato</b></li>
                </ul>
                <p>
                  El móvil del secuestro, tortura y asesinato de los 13 trabajadores de seguridad de dos socavones en el distrito de Pataz, La Libertad, fue el robo de 200 toneladas de material aurífero que habían conseguido acumular los mineros que laboraban para la empresa Libmar SAC.
                </p>
                <div class="detalle-noticia-image-container-123">
                    <img src="https://backend-zarel.onrender.com/static/img/noticias/peru/noticia3.png" alt="Imagen relacionada" class="detalle-noticia-image-content-123" />
                </div> 
               <p>
                 Según declaraciones de testigos ante la Fiscalía Provincial Corporativa contra la Criminalidad Organizada de La Libertad, un grupo de sujetos armados con fusiles de asalto, que supuestamente responden a las órdenes de Miguel Antonio Rodríguez Díaz, alias “Cuchillo”, fueron quienes asaltaron los dos socavones que explota Libmar SAC para la Compañía Minera Poderosa, dueña de los yacimientos.
                </p>
                """.strip(),
                estado=True
            ),
            OBJCategoria(
                id=3,
                titulo='Gobierno establece cadena perpetua para los que usen a menores de edad en actos de sicariato',
                url=base_url_peru + "noticia6.png",
                fecha="2025-05-19",
                hora="10:00",
                descripcion = """
                <ul>
                <li><b>La ley modifica el Código Penal, Decreto Legislativo 635</b></li>
                <li><b>POR USAR MENORES EN DELITOS: PENA SERÁ DE HASTA 12 AÑOS</b></li>
                <li><b>POR USAR MENORES EN SICARIATO O NARCOTRÁFICO: PENA SERÁ DE HASTA 25 AÑOS</b></li>
                </ul>
                <p>
                  El Poder Ejecutivo promulgó la ley que establece cadena perpetua para las personas que capten a menores de edad valiéndose de su posición, cargo o vínculo familiar, a fin de obligarlos a cometer delitos de sicariato.
                </p>
                <div class="detalle-noticia-image-container-123">
                    <img src="https://backend-zarel.onrender.com/static/img/noticias/peru/noticia5.png" alt="Imagen relacionada" class="detalle-noticia-image-content-123" />
                </div> 
               <p>
                 En ese sentido, se incorpora el artículo 129-Q con penas que van de 8 años de pena privativa de libertad hasta la cadena perpetua.
                 Dicho artículo señala que quien “mediante violencia, amenaza u otras formas de coacción, abuso de poder o de situación de vulnerabilidad capte e induzca o instigue persuadiendo a un menor de edad para la comisión de delitos será reprimido con pena privativa de libertad no menor de 8 ni mayor de 12 años”.
                </p>
                """.strip(),
                estado=True
            )
        ]
    }

    categoria_nombre = categoria   # ✅ Solo usar el string directo

    return datos.get(categoria_nombre, [])   # ✅ Esto está bien

# Configuración de la API de Google Generative AI
API_KEY = "AIzaSyCmjRN_xL07aRkftfoUba3nHW-_hkrZwnc"
genai.configure(api_key=API_KEY)

# Datos de la radio (constantes para acceso rápido)
RADIO_INFO = {
    "nombre": "Luminares",
    "año_fundacion": 2000,
    "ubicacion": "Huamachuco, Perú",
    "region": "Sierra de La Libertad",
    "fundadores": "Emprendedores locales",
    "objetivo": "Informar y entretener a la población peruana",
    "horario": "24 horas al día, 7 días a la semana",
    "contacto": {
        "telefono": "975-750-670",
        "email": "radio@luminares.com",
        "web": "https://paglumin.onrender.com/home"
    }
}

# Solo mantenemos el patrón de saludos para respuesta rápida
PATRON_SALUDO = re.compile(r'\b(hola|hl|mano|hi|hey|buenos dias|buenas tardes|buenas noches|saludos)\b')
RESPUESTA_SALUDO = "¡Hola! Soy Lumin AI. ¿En qué puedo ayudarte hoy?"
RESPUESTA_ERROR = "Disculpa, tuve un problema al procesar tu consulta. Por favor, intenta de nuevo."

def asistentechatbot(mensaje_usuario: str) -> str:
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
    # Configura la zona horaria de Perú (America/Lima)
    hora_peru = datetime.now(timezone('America/Lima')).strftime("%A %d de %B del %Y, %H:%M %p")
    
    try:
        # Configuración para Gemini
        model = genai.GenerativeModel(
            'gemini-1.5-flash',
            generation_config={
                "temperature": 0.7,
                "top_p": 0.95,
                "top_k": 40
            }
        )
        # Información sobre la radio para el contexto
        info_radio = f"""
        Información sobre Radio Luminares:
        - Nombre: {RADIO_INFO['nombre']}
        - Ubicación: {RADIO_INFO['ubicacion']}, {RADIO_INFO['region']}
        - Año de fundación: {RADIO_INFO['año_fundacion']}
        - Fundadores: {RADIO_INFO['fundadores']}
        - Objetivo: {RADIO_INFO['objetivo']}
        - Horario: {RADIO_INFO['horario']}
        - Contacto: Teléfono {RADIO_INFO['contacto']['telefono']}, Email {RADIO_INFO['contacto']['email']}, Web {RADIO_INFO['contacto']['web']}
        """
        
        # Prompt completo con contexto de la radio
        prompt = f"""
        Como Lumin AI, el asistente virtual de Radio Luminares, responde a la siguiente consulta: 
        "{consulta}"
        
        {info_radio}

        Instrucciones:
        -Si preguntan a que hora es, responde: {hora_peru}
        -Si preguntan sobre qué tipo de música se transmite, responde que se difunden principalmente música cristiana, música cultural .
        -Si pregunta, quien es villacorta vidal cristhian o cristhian aldair villacorta vidal?, responde es el ingeniero que me dio vida.
        -Quien creo el aplicativo, responde el aplicativo fue desarrollado por el ingeniero Cristhian Villacorta Vidal el cual esta ubicado en trujillo.
        -Si el usuario pregunta sobre la radio,Recien usa la informacion de la radio de lo contrario no uses.
        - No uses la información de la radio en la respuesta.
        -Si el usuario pregunta por luminares o radio responde con la informacion de la radio.
        - Si no, responde con conocimiento general.
        -Si te preguntan quien es el desarrollador, reponde me creo el desarrollador Villacorta Vidal Cristhian
        """
        
        response = model.generate_content(prompt)
        if response.text:
            return response.text.strip()
        else:
            return "Lo siento, no puedo responder a esa consulta en este momento. ¿Puedo ayudarte con información sobre Radio Luminares?"
    except Exception as e:
        return "Disculpa, no pude generar una respuesta. ¿Te interesa conocer algo específico sobre Radio Luminares?"


