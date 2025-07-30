from models.informacion import OBJCategoria
import google.generativeai as genai
import re
from collections import deque

def obtener_informacion(categoria: str):
    base_url_mundo = "https://backend-zarel-production.up.railway.app/static/img/noticias/mundo/"
    base_url_peru = "https://backend-zarel-production.up.railway.app/static/img/noticias/peru/"
    datos = {
        "Mundo": [
            OBJCategoria(
                id=1,
                titulo="Un fuerte Terremoto de magnitud 8,7 en Rusia activa múltiples alertas de tsunami en el océano Pacífico",
                url=base_url_mundo + "noticia1.png",
                fecha="2025-07-30",
                hora="09:05",
                descripcion = """
                <ul>
                <li><b>Un terremoto de magnitud 8,8 sacudió la península de Kamchatka, generando alertas de tsunami en países del Pacífico como Japón, México, Hawái y Alaska.</b></li>
                <li><b>Autoridades japonesas ordenaron evacuaciones por olas de hasta 3 metros, mientras embarcaciones se alejaban de la costa.</b></li>
                <li><b>Se reportaron daños estructurales en Rusia, incluyendo una guardería y varias localidades afectadas en Kamchatka y Paramushir.</b></li>
                </ul>
                <p>
                  El miércoles 30 de julio, un potente sismo de magnitud 8,8 se registró frente a las costas de la península de Kamchatka, al este de Rusia. El movimiento, que ocurrió a 18 km de profundidad, generó alertas de tsunami en varios países del océano Pacífico, incluyendo Japón, México y territorios como Hawái y Alaska. Aunque en Japón el sismo fue poco perceptible, autoridades activaron protocolos de evacuación en zonas costeras de múltiples prefecturas, anticipando olas de hasta tres metros.
                </p>
                <div class="detalle-noticia-image-container-123">
                    <img src="https://backend-zarel.onrender.com/static/img/noticias/mundo/noticia2.png" alt="Imagen relacionada" class="detalle-noticia-image-content-123" />
                </div> 
               <p>
                Imágenes transmitidas por medios japoneses mostraron a personas evacuadas en Hokkaido refugiándose en techos y bajo carpas, mientras barcos pesqueros se alejaban de los puertos. En Rusia, se reportaron daños materiales, como el colapso parcial de una guardería y afectaciones en edificaciones de Kamchatka y la isla Paramushir. La NOAA estadounidense también emitió alertas para varias zonas costeras, reflejando el alcance regional del evento sísmico.
                </p>
                """.strip(),
                estado=True
            ),
            OBJCategoria(
                id=2,
                titulo="Jordania y Emiratos Árabes Unidos realizaron un nuevo envío aéreo con 16 toneladas de ayuda humanitaria para Gaza, con el fin de aliviar la crisis alimentaria",
                url=base_url_mundo + "noticia3.png",
                fecha="2025-07-30",
                hora="11:10",
                descripcion = """
                <ul>
                <li><b>Jordania y EAU lanzaron 16 toneladas de alimentos y leche en Gaza, sumando ya más de 70 toneladas en total.</b></li>
                <li><b>Bélgica se suma a la operación con un avión cargado de ayuda por 600 mil euros.</b></li>
                <li><b>La ONU alerta posible hambruna: ya hay 154 muertes por desnutrición, incluyendo 89 niños.</b></li>
                </ul>
                <p>
                 La ayuda aérea enviada por Jordania, Emiratos Árabes Unidos y próximamente Bélgica intenta mitigar la grave situación humanitaria en Gaza, donde el bloqueo ha dejado a cientos de miles sin acceso regular a alimentos. Aunque estas operaciones suman toneladas de suministros, organizaciones advierten que los lanzamientos no siempre son efectivos, ya que muchos paquetes caen en zonas inaccesibles o en áreas de combate, lo que limita su impacto real.
                </p>
                <div class="detalle-noticia-image-container-123">
                    <img src="https://backend-zarel.onrender.com/static/img/noticias/mundo/noticia4.png" alt="Imagen relacionada" class="detalle-noticia-image-content-123" />
                </div> 
               <p>
                    Mientras tanto, la crisis alimentaria sigue empeorando. Las cifras son alarmantes: más de medio millón de personas viven bajo condiciones similares a una hambruna y cientos de miles de niños enfrentan desnutrición aguda. La ONU ha advertido que Gaza podría ser oficialmente declarada en hambruna si las condiciones no mejoran pronto, especialmente ante el aumento sostenido de muertes por hambre, enfermedades y falta de atención médica.
                </p>
                """.strip(),
                estado=True
            ),
            OBJCategoria(
                id=3,
                titulo='SpaceX revela una nueva versión mejorada de su nave Starship, diseñada para futuras misiones hacia Marte',
                url=base_url_mundo + "noticia5.png",
                fecha="2025-07-30",
                hora="06:40",
                descripcion = """
                <ul>
                <li><b>SpaceX trasladó su prototipo Starship V2 a Texas para iniciar pruebas clave antes de futuras misiones a Marte.</b></li>
                <li><b>Elon Musk anunció que la versión V3 podría estar lista para ser lanzada a finales del año.</b></li>
                <li><b>El desarrollo de Starship busca reducir costos, facilitar misiones lunares y abrir camino a la colonización de Marte.</b></li>
                </ul>
                <p>
                 SpaceX ha comenzado una nueva fase en su programa de desarrollo espacial al trasladar el prototipo Starship V2 a su base de Texas. El vehículo, considerado un paso importante en la misión de llevar humanos a Marte, fue movilizado a la torre de lanzamiento en South Texas, donde la empresa realiza sus pruebas principales. Elon Musk destacó que la próxima versión, V3, podría estar lista para lanzarse antes de fin de año.
                </p>
                <div class="detalle-noticia-image-container-123">
                    <img src="https://backend-zarel.onrender.com/static/img/noticias/mundo/noticia6.png" alt="Imagen relacionada" class="detalle-noticia-image-content-123" />
                </div> 
               <p>
                    Starship representa un avance clave en la industria aeroespacial por ser un cohete superpesado y completamente reutilizable. Su éxito podría transformar el acceso al espacio, reduciendo drásticamente los costos y facilitando misiones como el programa lunar Artemis. Además, SpaceX proyecta que sus futuras operaciones desde Florida aumentarán la capacidad de fabricación y frecuencia de lanzamientos.
                </p>
                """.strip(),
                estado=True
            )
        ],
        "Peru": [
            OBJCategoria(
                id=1,
                titulo="Alerta de tsunami en Perú: regiones afectadas y horario actualizado del posible impacto de las olas en el litoral peruano",
                url=base_url_peru + "noticia1.png",
                fecha="2025-07-30",
                hora="08:35",
                descripcion = """
                <ul>
                <li><b>Se cerraron 65 puertos y playas como la Costa Verde y La Punta ante la alerta de tsunami en el litoral peruano</b></li>
                <li><b>La llegada del tsunami a la costa norte del Perú se estima para las 12:15 p.m., según la Marina de Guerra y el Indeci.</b></li>
                <li><b>Algunos pescadores en Chiclayo ignoraron las advertencias y salieron a pescar pese a la prohibición.</b></li>
                </ul>
                <p>
                  Un fuerte sismo de magnitud 8.7 registrado en la península de Kamchatka, Rusia, activó una alerta de tsunami en varias zonas del Pacífico, incluyendo el Perú. Ante esta situación, las autoridades peruanas cerraron 65 puertos y restringieron el acceso a playas como La Punta, la Costa Verde y otras del litoral, además de evacuar a los residentes cercanos al mar. Defensa Civil emitió una alerta masiva a los celulares de la población, recomendando el cierre total de playas hasta que se levante la advertencia. La Dirección de Hidrografía y Navegación informó que las olas podrían llegar a la costa norte del país alrededor de las 12:15 p.m., basándose en datos del arribo a la Isla Galápagos.
                </p>
                <div class="detalle-noticia-image-container-123">
                    <img src="https://backend-zarel.onrender.com/static/img/noticias/peru/noticia2.png" alt="Imagen relacionada" class="detalle-noticia-image-content-123" />
                </div> 
               <p>
                 En respuesta, instituciones como Indeci, la Presidencia y la Municipalidad de Lima han articulado acciones preventivas, monitoreo constante y comunicación con los distritos costeros. No obstante, algunos ciudadanos han ignorado las medidas de seguridad; por ejemplo, pescadores de Chiclayo salieron al mar en sus caballitos de totora pese a las advertencias, lo que pone en riesgo sus vidas ante la posible llegada del tsunami.
                </p>
                """.strip(),
                estado=True
            ),
            OBJCategoria(
                id=2,
                titulo='Dina Boluarte no mencionó en su mensaje que tiene previsto firmar un contrato para comprar 24 aviones de combate',
                url=base_url_peru + "noticia3.png",
                fecha="2025-07-30",
                hora="08:00",
                descripcion = """
                <ul>
                <li><b>Dina Boluarte evitó mencionar en su discurso la compra de 24 aviones de combate para modernizar la Fuerza Aérea.</b></li>
                <li><b>El contrato incluiría aeronaves como el Gripen E, con tecnología avanzada y capacidad supersónica.</b></li>
                <li><b>La inversión supera los 3 mil millones de dólares y ha generado debate entre seguridad nacional y necesidades sociales</b></li>
                </ul>
                <p>
                 Durante su mensaje por Fiestas Patrias, la presidenta Dina Boluarte evitó mencionar la compra de 24 aviones de combate, una medida destinada a renovar la capacidad de la Fuerza Aérea del Perú. Aunque el discurso escrito incluía este anuncio, fue omitido en su intervención ante el Congreso. Según voceros del gobierno, la adquisición busca reemplazar a los antiguos Mirage 2000, superados tecnológicamente. Uno de los modelos evaluados es el Gripen E, un caza sueco capaz de volar a más de 2.400 km/h y operar en condiciones adversas.
                </p>
                <div class="detalle-noticia-image-container-123">
                    <img src="https://backend-zarel.onrender.com/static/img/noticias/peru/noticia4.png" alt="Imagen relacionada" class="detalle-noticia-image-content-123" />
                </div> 
               <p>
                  Esta compra representa una de las mayores inversiones en defensa en décadas, con un presupuesto estimado de más de tres mil millones de dólares. Mientras sectores militares y técnicos la consideran necesaria, otros, como congresistas y organizaciones civiles, cuestionan su prioridad frente a demandas sociales urgentes como salud, educación e infraestructura. Aunque aún no hay contrato firmado, el gobierno da señales claras de avanzar con la modernización del poder aéreo.
                </p>
                """.strip(),
                estado=True
            ),
            OBJCategoria(
                id=3,
                titulo='El Consejo Regional de La Libertad convocará a César Acuña para que responda por millonarias licitaciones otorgadas a una joven empresaria.',
                url=base_url_peru + "noticia5.png",
                fecha="2025-05-19",
                hora="10:00",
                descripcion = """
                <ul>
                <li><b>El Consejo Regional de La Libertad citará a César Acuña y a sus gerentes por contratos superiores a S/ 300 millones.</b></li>
                <li><b>La empresa beneficiada está liderada por una joven de 23 años sin experiencia en obras públicas.</b></li>
                <li><b>Las reuniones previas entre la empresaria y altos funcionarios quedaron registradas oficialmente.</b></li>
                </ul>
                <p>
                  El Consejo Regional de La Libertad ha decidido convocar al gobernador César Acuña y a sus principales funcionarios para que den explicaciones sobre licitaciones por más de S/ 300 millones adjudicadas a una empresa dirigida por Lucero Nicole Coca Condori, una joven de 23 años sin experiencia previa en obras públicas. Entre los citados figuran Martín Namay, gerente general, y Jorge Bringas, gerente de Infraestructura. Las obras en cuestión son el Corredor Vial Norte (S/ 121 millones) y el Hospital de Virú (S/ 194 millones).
                </p>
                <div class="detalle-noticia-image-container-123">
                    <img src="https://backend-zarel.onrender.com/static/img/noticias/peru/noticia6.png" alt="Imagen relacionada" class="detalle-noticia-image-content-123" />
                </div> 
               <p>
                 Según el consejero Robert de la Cruz, la empresaria y sus allegados sostuvieron reuniones previas con autoridades del Gobierno Regional. El padre de Lucero, Juan Carlos Coca, se reunió con Acuña el 8 de marzo de 2024, mientras que ella se entrevistó con los gerentes Bringas y Namay en marzo y mayo, respectivamente. Estas visitas fueron registradas en los cuadernos oficiales, lo que ha generado sospechas sobre la transparencia del proceso de adjudicación.
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


