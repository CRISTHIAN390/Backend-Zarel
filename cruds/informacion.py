from models.informacion import OBJCategoria
import google.generativeai as genai
import re
from collections import deque



def procesarInfo(data):
    # Puedes ignorar los datos por ahora y solo devolver datos de prueba
    documentos = [
        {
            "fecha": "2024-01-15",
            "monto": 150.50,
            "url": "https://example.com/documento1.pdf"
        },
        {
            "fecha": "2024-02-20",
            "monto": 299.99,
            "url": "https://example.com/documento2.pdf"
        }
    ]
    return documentos








def obtener_informacion(categoria: str):
    base_url_mundo = "https://backend-zarel-production.up.railway.app/static/img/noticias/mundo/"
    base_url_peru = "https://backend-zarel-production.up.railway.app/static/img/noticias/peru/"
    datos = {
        "Mundo": [
            OBJCategoria(
                id=1,
                titulo="Israel derribó otro edificio en la ciudad de Gaza que estaba siendo utilizado por militantes de Hamas",
                url=base_url_mundo + "noticia1.png",
                fecha="2025-09-13",
                hora="08:05",
                descripcion = """
                <ul>
                <li><b>El Ejército israelí derribó la torre Nour en Ciudad de Gaza, un edificio de 12 plantas que según las FDI era utilizado por Hamas para planear y ejecutar ataques.</b></li>
                <li><b>Los bombardeos y demoliciones han dejado sin hogar a decenas de miles de palestinos, con más de 53.000 personas que han perdido sus viviendas en menos de una semana.</b></li>
                <li><b>Más de 250.000 habitantes han abandonado Ciudad de Gaza tras la intensificación de los ataques, en un desplazamiento masivo hacia el sur de la Franja.</b></li>
                </ul>
                <p>
                  El Ejército israelí derribó un rascacielos de 12 plantas en Gaza, identificado como la torre Nour, tras emitir una orden de evacuación. Según las FDI, el inmueble era utilizado por Hamas como centro operativo para planear ataques. Este hecho se suma a una serie de bombardeos que han destruido varios edificios en la capital gazatí, incrementando la devastación en la zona.
                </p>
                <div class="detalle-noticia-image-container-123">
                    <img src="https://backend-zarel.onrender.com/static/img/noticias/mundo/noticia2.png" alt="Imagen relacionada" class="detalle-noticia-image-content-123" />
                </div> 
               <p>
                La ofensiva ha provocado graves consecuencias humanitarias: más de 53.000 palestinos han perdido sus hogares en pocos días y al menos 250.000 personas se han desplazado hacia el sur del enclave en busca de seguridad. Además de las torres residenciales, cientos de tiendas de campaña y viviendas fueron destruidas, dejando a miles de familias sin refugio en medio de la crisis.
                </p>
                """.strip(),
                estado=True
            ),
            OBJCategoria(
                id=2,
                titulo="Rusia efectuó un nuevo ataque de gran escala contra Ucrania, en el que lanzó un misil y 164 drones durante la noche.",
                url=base_url_mundo + "noticia3.png",
                fecha="2025-09-13",
                hora="8:15",
                descripcion = """
                <ul>
                <li><b>Rusia lanzó un ataque nocturno contra Ucrania con un misil balístico y 164 drones, de los cuales 137 fueron neutralizados por la defensa ucraniana.</b></li>
                <li><b>En paralelo, Rusia y Bielorrusia iniciaron maniobras militares estratégicas cerca de la frontera polaca, lo que generó preocupación en la OTAN.</b></li>
                <li><b>El secretario general de la OTAN, Mark Rutte, denunció múltiples violaciones del espacio aéreo aliado por drones rusos y anunció una nueva iniciativa de defensa llamada Centinela oriental.</b></li>
                </ul>
                <p>
                 Durante la noche, Rusia ejecutó un ataque masivo contra Ucrania empleando un misil balístico Iskander-M y más de 160 drones de distintos modelos. La Fuerza Aérea ucraniana informó que logró derribar o neutralizar 137 de estos aparatos, aunque se registraron impactos en nueve zonas y fragmentos en otras tres. Las acciones defensivas incluyeron el uso de aviación, sistemas antiaéreos y unidades de guerra electrónica para repeler la ofensiva.
                </p>
                <div class="detalle-noticia-image-container-123">
                    <img src="https://backend-zarel.onrender.com/static/img/noticias/mundo/noticia4.png" alt="Imagen relacionada" class="detalle-noticia-image-content-123" />
                </div> 
               <p>
                    Al mismo tiempo, Rusia y Bielorrusia pusieron en marcha la fase activa de los ejercicios militares Západ-2025 cerca de Minsk, a menos de 500 kilómetros de Polonia. Estas maniobras, junto con recientes incursiones aéreas rusas en territorio aliado, llevaron a la OTAN a reforzar su flanco oriental. El secretario general, Mark Rutte, calificó las violaciones del espacio aéreo como peligrosas y reiteró que Rusia cruzó los límites de seguridad de la Alianza, anunciando la creación de la iniciativa Centinela oriental para fortalecer la defensa regional.
                </p>
                """.strip(),
                estado=True
            ),
            OBJCategoria(
                id=3,
                titulo='Fitch señaló que la deuda soberana de Francia se vio afectada por la incertidumbre fiscal del gobierno de Macron',
                url=base_url_mundo + "noticia5.png",
                fecha="2025-09-13",
                hora="9:30",
                descripcion = """
                <ul>
                <li><b>Fitch bajó la calificación de la deuda francesa de “AA-” a “A+” por la incertidumbre política y fiscal.</b></li>
                <li><b>La caída de Bayrou y el nombramiento de Lecornu complican la aprobación del presupuesto 2026.</b></li>
                <li><b>Protestas sociales y mayor endeudamiento acercan a Francia a niveles similares a Italia.</b></li>
                </ul>
                <p>
                 La agencia Fitch redujo la calificación de la deuda francesa a “A+”, señalando la inestabilidad política y la falta de claridad fiscal como los principales obstáculos para una consolidación presupuestaria. Este ajuste refleja un mayor riesgo de vulnerabilidad frente a cambios económicos adversos y se produce en un contexto en el que el gobierno de Emmanuel Macron enfrenta divisiones parlamentarias y la necesidad de aprobar el presupuesto de 2026.
                </p>
                <div class="detalle-noticia-image-container-123">
                    <img src="https://backend-zarel.onrender.com/static/img/noticias/mundo/noticia6.png" alt="Imagen relacionada" class="detalle-noticia-image-content-123" />
                </div> 
               <p>
                   El nuevo primer ministro, Sébastien Lecornu, asumió la tarea de estabilizar la situación política tras la salida de Bayrou, pero debe lidiar con la presión social y la oposición parlamentaria. Mientras se evalúa la posibilidad de incluir impuestos a las grandes fortunas, casi 200.000 manifestantes salieron a las calles exigiendo mejoras salariales y mayor equidad fiscal. En este escenario, el futuro de las finanzas francesas será revisado nuevamente por S&P Global en noviembre, aumentando la incertidumbre económica.
                </p>
                """.strip(),
                estado=True
            )
        ],
        "Peru": [
            OBJCategoria(
                id=1,
                titulo="Marcha por el retiro de AFP EN VIVO: manifestantes demandan una nueva liberación de fondos y se oponen a la reforma de pensiones",
                url=base_url_peru + "noticia1.png",
                fecha="2025-09-13",
                hora="09:35",
                descripcion = """
                <ul>
                <li><b>Ciudadanos marchan desde la Plaza San Martín para rechazar la reforma del sistema de pensiones y exigir nuevo retiro de fondos AFP.</b></li>
                <li><b>La ley fija pensión mínima de 600 soles con 20 años de aporte, obliga a independientes a cotizar desde 2028 y eleva la jubilación anticipada a 55 años.</b></li>
                <li><b>Jóvenes desde 18 años serán afiliados automáticamente, y los menores de 40 no podrán retirar el 95.5% de su fondo al jubilarse.</b></li>
                </ul>
                <p>
                  Este sábado 13 de septiembre, ciudadanos se movilizaron en Lima y otras ciudades para expresar su rechazo a la reforma previsional. La protesta, convocada de manera independiente en redes sociales, busca exigir un nuevo retiro de fondos de las AFP y denunciar los cambios que consideran perjudiciales para los afiliados. Además, la marcha también levantó la voz contra la creciente delincuencia y la ola de extorsiones en el país.
                </p>
                <div class="detalle-noticia-image-container-123">
                    <img src="https://backend-zarel.onrender.com/static/img/noticias/peru/noticia2.png" alt="Imagen relacionada" class="detalle-noticia-image-content-123" />
                </div> 
               <p>
                 La reforma establece que todos los retiros de AFP quedan prohibidos y fija una pensión mínima de 600 soles, condicionada a 20 años de aportes. También obliga a los trabajadores independientes a cotizar desde 2028 con un descuento entre 2% y 5%, eleva la edad para la jubilación anticipada a 55 años, y limita el acceso al 95.5% del fondo a quienes tengan menos de 40 años. Asimismo, dispone que toda persona mayor de 18 años sea afiliada obligatoriamente a una AFP.
                </p>
                """.strip(),
                estado=True
            ),
            OBJCategoria(
                id=2,
                titulo='Ibai Llanos transmitirá en pantalla grande el anuncio del ganador del Mundial de desayunos',
                url=base_url_peru + "noticia3.png",
                fecha="2025-09-13",
                hora="09:51",
                descripcion = """
                <ul>
                <li><b>La Municipalidad de Miraflores organiza un evento comunitario para alentar votos por el pan con chicharrón en el Mundial de desayunos de Ibai Llanos.</b></li>
                <li><b>El encuentro se realizará en el pasaje Porta con pantalla gigante, participación de foodies e influencers, y la oferta de chicharronerías locales.</b></li>
                <li><b>El pan con chicharrón, desayuno típico peruano, compite contra otros países en una dinámica global creada por el streamer español.</b></li>
                </ul>
                <p>
                 Este sábado 13 de septiembre, Miraflores será escenario de un evento especial organizado por la municipalidad, donde vecinos y visitantes podrán reunirse para apoyar al pan con chicharrón en la semifinal del Mundial de desayunos impulsado por Ibai Llanos. La jornada contará con foodies, influencers, pantallas gigantes y códigos QR para facilitar la votación en línea, además de degustaciones ofrecidas por diversas chicharronerías del distrito.
                </p>
                <div class="detalle-noticia-image-container-123">
                    <img src="https://backend-zarel.onrender.com/static/img/noticias/peru/noticia4.png" alt="Imagen relacionada" class="detalle-noticia-image-content-123" />
                </div> 
               <p>
                  La competencia, transmitida por el popular streamer español en sus plataformas digitales, busca elegir el mejor desayuno del mundo. Perú participa con su tradicional pan con chicharrón, preparado con pan francés, cerdo frito, camote dorado y salsa criolla, un plato que forma parte de la identidad gastronómica del país y que suele disfrutarse en familia los domingos o en celebraciones especiales.
                </p>
                """.strip(),
                estado=True
            ),
            OBJCategoria(
                id=3,
                titulo='El BCR recortó la tasa de interés de referencia a 4,25%; analizan las razones, el impacto en el país y la posibilidad de un nuevo ajuste.',
                url=base_url_peru + "noticia5.png",
                fecha="2025-09-13",
                hora="10:00",
                descripcion = """
                <ul>
                <li><b>El BCR redujo la tasa de interés de referencia en 25 puntos básicos, situándola en 4,25%, su nivel más bajo en tres años.</b></li>
                <li><b>Según Adrián Armas, la decisión responde a una inflación controlada (2,2%) y a un crecimiento económico cercano al 3%.</b></li>
                <li><b>El ajuste ya era anticipado por el mercado y se espera un impacto marginal, con proyecciones de expansión del crédito de 5% este año.</b></li>
                </ul>
                <p>
                  El Banco Central de Reserva (BCR) decidió recortar la tasa de interés de referencia a 4,25%, lo que la ubica cerca de un nivel considerado neutral para la economía. Este es el nivel más bajo desde 2022, y la medida se tomó en un contexto de inflación controlada y de expectativas de crecimiento anual de alrededor del 3%. Adrián Armas, gerente central de Estudios Económicos, señaló que el mercado ya anticipaba este ajuste y que la medida fue vista como necesaria para mantener la estabilidad macroeconómica.
                </p>
                <div class="detalle-noticia-image-container-123">
                    <img src="https://backend-zarel.onrender.com/static/img/noticias/peru/noticia6.png" alt="Imagen relacionada" class="detalle-noticia-image-content-123" />
                </div> 
               <p>
                 Pese al contexto electoral, el BCR considera que la economía peruana mantiene dinamismo y que las inversiones actuales contribuirán a fortalecer la capacidad productiva en los próximos años. El impacto inmediato de la reducción se estima marginal, ya que buena parte de los agentes financieros había previsto el cambio; sin embargo, se mantiene una proyección de expansión del crédito del 5% para 2025, respaldada por una reciente aceleración en los préstamos.
                </p>
                """.strip(),
                estado=True
            )
        ]
    }




















    categoria_nombre = categoria   # ✅ Solo usar el string directo

    return datos.get(categoria_nombre, [])   # ✅ Esto está bien

# Configuración de la API de Google Generative AI    AIzaSyCmjRN_xL07aRkftfoUba3nHW-_hkrZwnc
API_KEY = "AIzaSyAQ60ndktxOiAopNpE_CHYxV6QSs2-oyxs"
genai.configure(api_key=API_KEY)
 
# Datos de la radio (constantes para acceso rápido)
RADIO_INFO = {
    "nombre": "Radio Luminares",
    "año_fundacion": 2000,
    "ubicacion": "Huamachuco, Perú",
    "region": "Sierra de La Libertad",
    "fundadores": "Emprendedores locales",
    "objetivo": "Informar y entretener a la población peruana",
    "horario": "24/7 durante toda la semana",
    "contacto": {
        "telefono": "975-750-670",
        "email": "radio@luminares.com",
        "web": "https://paglumin.onrender.com/home"
    }
}
 
 
# Solo mantenemos el patrón de saludos para respuesta rápida
PATRON_SALUDO = re.compile(r'\b(hola|hl|mano|hi|hey|buenos dias|que tal|buenas|buenas tardes|buenas noches|saludos)\b')
RESPUESTA_SALUDO = "¡Hola! Soy Lumin AI. ¿En qué puedo ayudarte hoy?"
RESPUESTA_ERROR = "Ups... algo salió mal al procesar tu mensaje 😓. ¿Podrías intentarlo otra vez, por favor?"


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
        Actúa como Lumin AI, el asistente virtual de Radio Luminares, responde a la siguiente consulta con un tono amigable, claro y profesional: 
        "{consulta}"
        
        {info_radio}

        Instrucciones:
        - Si preguntan sobre el tipo de música que se transmite, responde que se difunden música cristiana y música cultural 🎶.
        - Si preguntan quién es Villacorta Vidal Cristhian o Cristhian Aldair Villacorta Vidal, responde: "Es el ingeniero que me diseñó y programó."
        - Si preguntan quién creó el aplicativo, la app o el APK, responde: "El aplicativo fue desarrollado por el Ing. Villacorta Vidal 👨🏻‍💻."
        - No menciones información sobre Radio Luminares a menos que se solicite explícitamente.
        - Si se menciona luminares, radio o radio luminares, responde con información oficial de la radio.
        - Si no se menciona nada relacionado con la radio, responde con conocimiento general.
        - Si preguntan quién es el desarrollador, responde incluyendo este enlace 👉 https://play.google.com/store/apps/dev?id=7894508111389002888&hl=es.
        """
        response = model.generate_content(prompt)
        if response.text:
            return response.text.strip()
        else:
            return "Lo siento, no puedo responder a esa consulta en este momento. ¿Puedo ayudarte con información sobre Radio Luminares?"
    except Exception as e:
            return "Disculpa, no pude generar una respuesta. ¿Te interesa conocer algo sobre Radio Luminares?"


