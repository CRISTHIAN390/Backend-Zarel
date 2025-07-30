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


