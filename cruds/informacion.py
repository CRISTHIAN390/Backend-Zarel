from models.informacion import OBJCategoria
from google import genai
from google.genai import types
import re
from collections import deque
import os



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
                titulo="EE.UU. impone sanciones al presidente colombiano Gustavo Petro por presunto vínculo con el narcotráfico",
                url=base_url_mundo + "noticia1.png",
                fecha="2026-10-23",
                hora="12:35",
                descripcion = """
                <ul>
                <li><b>El gobierno de Donald Trump incluyó a Gustavo Petro, su familia y su ministro del Interior en la lista OFAC del Departamento del Tesoro.</b></li>
                <li><b>Washington acusa a Petro de facilitar el aumento histórico en la producción de cocaína y de mantener nexos con el régimen de Nicolás Maduro.</b></li>
                <li><b>Petro rechazó las sanciones calificándolas de injustas y paradójicas, asegurando que su gobierno ha decomisado cantidades récord de droga.</b></li>
                </ul>
                <p>
                  El gobierno de Estados Unidos, encabezado por Donald Trump, sancionó al presidente colombiano Gustavo Petro, a miembros de su familia y a su ministro del Interior al incluirlos en la lista OFAC, que bloquea activos y restringe transacciones con ciudadanos estadounidenses. Washington sostiene que, bajo el mandato de Petro, la producción de cocaína alcanzó niveles sin precedentes, lo que representa una amenaza para la seguridad y la economía de EE.UU. Además, el Departamento del Tesoro lo acusa de haberse aliado con el régimen de Nicolás Maduro en Venezuela y de participar en actividades relacionadas con el narcotráfico internacional.
                </p>
                <div class="detalle-noticia-image-container-123">
                    <img src="https://backend-zarel.onrender.com/static/img/noticias/mundo/noticia2.png" alt="Imagen relacionada" class="detalle-noticia-image-content-123" />
                </div> 
               <p>
                Petro respondió calificando la medida como una paradoja, argumentando que su administración ha sido una de las más activas en la lucha contra el narcotráfico, con cifras récord de decomisos. Las sanciones llegan poco después de tensiones diplomáticas entre ambos países, tras las críticas del mandatario colombiano hacia acciones estadounidenses en el Caribe. Con esta decisión, cualquier bien o cuenta vinculada a Petro en territorio estadounidense queda bloqueada, y se prohíbe a ciudadanos y empresas de EE.UU. realizar operaciones con los sancionados.
                </p>
                """.strip(),
                estado=True
            ),
            OBJCategoria(
                id=2,
                titulo="Trump refuerza su poder militar y la presencia de la CIA en el Caribe: crecen las tensiones con Venezuela y Maduro",
                url=base_url_mundo + "noticia3.png",
                fecha="2025-10-24",
                hora="15:40",
                descripcion = """
                <ul>
                <li><b>Estados Unidos realiza el mayor despliegue militar en el Caribe en décadas, con buques de guerra, bombarderos y operaciones de inteligencia de la CIA cerca de Venezuela.</b></li>
                <li><b>Washington presenta la operación como parte de su lucha antidrogas, pero analistas y líderes regionales creen que busca presionar o derrocar al presidente Nicolás Maduro.</b></li>
                <li><b>EE.UU. ofrece hasta 50 millones de dólares por información que lleve a la captura de Maduro, mientras mantiene sanciones y un bloqueo diplomático desde 2019.</b></li>
                </ul>
                <p>
                 El gobierno de Donald Trump ha intensificado su postura frente a Venezuela con un amplio despliegue militar en el Caribe, el más grande en décadas. La presencia de destructores, bombarderos B-52, marines y aviones de vigilancia se enmarca oficialmente en una estrategia contra el narcotráfico, aunque muchos expertos y gobiernos de la región ven en ello una maniobra de presión para forzar un cambio de régimen. Además del componente militar, Trump autorizó operaciones de la CIA en territorio venezolano, aumentando la tensión con el gobierno de Nicolás Maduro. La Casa Blanca sostiene que las acciones buscan frenar el tráfico de drogas y restaurar la democracia, mientras crece el debate sobre su legalidad y verdadero propósito.
                </p>
                <div class="detalle-noticia-image-container-123">
                    <img src="https://backend-zarel.onrender.com/static/img/noticias/mundo/noticia4.png" alt="Imagen relacionada" class="detalle-noticia-image-content-123" />
                </div> 
               <p>
                    En paralelo, Washington ha elevado a 50 millones de dólares la recompensa por la captura de Maduro y mantiene severas sanciones económicas contra Caracas. Sin embargo, pese a la presión internacional, el mandatario venezolano sigue contando con el respaldo de su cúpula militar y aliados políticos, quienes temen represalias judiciales si se rebelan. Los analistas coinciden en que el ejército será clave para cualquier eventual transición, pero dudan de que las medidas estadounidenses consigan quebrar su lealtad. En un contexto de crisis económica y aislamiento diplomático, el conflicto entre ambos gobiernos parece entrar en una nueva etapa de confrontación política y militar.
                </p>
                """.strip(),
                estado=True
            ),
            OBJCategoria(
                id=3,
                titulo='Atlas: el nuevo navegador de OpenAI que desafía el dominio de Google en las búsquedas web',
                url=base_url_mundo + "noticia5.png",
                fecha="2025-10-24",
                hora="16:14",
                descripcion = """
                <ul>
                <li><b>OpenAI lanzó ChatGPT Atlas, un navegador impulsado por inteligencia artificial que elimina la barra de direcciones y se centra en búsquedas conversacionales.</b></li>
                <li><b>El navegador busca posicionarse frente a gigantes como Google Chrome y Microsoft Edge, ofreciendo incluso un modo de agente automático para realizar búsquedas por cuenta del usuario.</b></li>
                <li><b>El lanzamiento llega mientras Google enfrenta juicios antimonopolio y crece el uso de modelos de lenguaje como ChatGPT para realizar consultas en internet</b></li>
                </ul>
                <p>
                    OpenAI ha presentado Atlas, un navegador web creado alrededor de ChatGPT que promete transformar la manera en que las personas buscan información en línea. A diferencia de los navegadores tradicionales, Atlas elimina la barra de direcciones e integra directamente la inteligencia artificial para ofrecer respuestas personalizadas en lugar de simples enlaces. Sam Altman, CEO de OpenAI, explicó que este navegador representa un nuevo paso para monetizar la expansión de su ecosistema de IA, que ya cuenta con más de 800 millones de usuarios semanales. Además, Atlas incorporará un modo de agente pago que podrá realizar búsquedas y tareas por cuenta propia, brindando una experiencia más automatizada y eficiente.
                </p>
                <div class="detalle-noticia-image-container-123">
                    <img src="https://backend-zarel.onrender.com/static/img/noticias/mundo/noticia6.png" alt="Imagen relacionada" class="detalle-noticia-image-content-123" />
                </div> 
                <p>
                   Pese al entusiasmo, algunos analistas se muestran cautelosos ante la posibilidad de que Atlas desplace a gigantes como Chrome o Edge, dado que muchos usuarios prefieren mantenerse en entornos familiares. Sin embargo, el lanzamiento coincide con el creciente cuestionamiento al dominio de Google en el mercado de las búsquedas, tras su reciente fallo por monopolio ilegal. En este contexto, la propuesta de OpenAI apunta a capitalizar el auge de los modelos de lenguaje y a redefinir cómo los internautas acceden a la información en una nueva era de búsquedas impulsadas por IA.
                </p>
                """.strip(),
                estado=True
            )
        ],
        "Peru": [
            OBJCategoria(
                id=1,
                titulo="Agua Marina se retira temporalmente tras atentado en Chorrillos y pide unión y calma al país",
                url=base_url_peru + "noticia1.png",
                fecha="2025-10-24",
                hora="16:35",
                descripcion = """
                <ul>
                <li><b>La agrupación de cumbia anunció una pausa indefinida para recuperarse física y emocionalmente del atentado ocurrido durante su concierto en Chorrillos.</b></li>
                <li><b>Los hermanos Quiroga afirmaron que volverán a los escenarios “cuando sea el momento”, priorizando la salud y la paz de sus integrantes.</b></li>
                <li><b>En su comunicado, el grupo también expresó su apoyo a quienes protestan por la inseguridad y llamó a la unidad y empatía entre los peruanos.</b></li>
                </ul>
                <p>
                  El reconocido grupo de cumbia Agua Marina sorprendió a sus seguidores al anunciar su retiro temporal de los escenarios tras el atentado ocurrido durante su presentación en el Círculo Militar de Chorrillos. En el ataque, cuatro músicos resultaron heridos, aunque todos lograron sobrevivir. A través de un comunicado difundido en sus redes sociales, los hermanos Quiroga explicaron que necesitan un tiempo para recuperarse “física y mentalmente” de lo sucedido, asegurando que su regreso ocurrirá “cuando sea el momento y de la mano de Dios”. El anuncio generó muestras masivas de apoyo y solidaridad por parte del público.
                </p>
                <div class="detalle-noticia-image-container-123">
                    <img src="https://backend-zarel.onrender.com/static/img/noticias/peru/noticia2.png" alt="Imagen relacionada" class="detalle-noticia-image-content-123" />
                </div> 
               <p>
                 En el mismo mensaje, la agrupación también aprovechó para pronunciarse sobre la situación social del país, rechazando los ataques hacia los ciudadanos que participaron en la marcha nacional contra la inseguridad. Agua Marina enfatizó su compromiso con la paz, la empatía y la unión entre los peruanos, señalando que la música debe servir como un puente que conecte y no como un motivo de división. Con este mensaje, el grupo reafirmó su papel no solo como referente musical, sino también como voz de esperanza y reflexión en momentos difíciles para el país.
                </p>
                """.strip(),
                estado=True
            ),
            OBJCategoria(
                id=2,
                titulo='Desconfianza histórica: más del 80% de peruanos no cree en la Policía Nacional, según el INEI',
                url=base_url_peru + "noticia3.png",
                fecha="2025-10-24",
                hora="16:51",
                descripcion = """
                <ul>
                <li><b>La confianza en la Policía Nacional del Perú cayó al 14.2%, su nivel más bajo en una década, reveló el INEI.</b></li>
                <li><b>Casi 1.000 agentes han sido detenidos en lo que va del año por delitos que incluyen violencia, corrupción y homicidio.</b></li>
                <li><b>Expertos señalan que la PNP necesita resultados concretos contra la delincuencia y reformas internas para recuperar la credibilidad ciudadana.</b></li>
                </ul>
                <p>
                 La desconfianza hacia la Policía Nacional del Perú (PNP) alcanzó un punto crítico: solo el 14.2% de los ciudadanos afirma confiar en la institución, según un reciente estudio del INEI. Este nivel representa la cifra más baja de los últimos diez años y refleja un deterioro constante de la imagen policial. Los cuestionamientos aumentaron tras el asesinato del joven rapero Eduardo Ruiz “Trvko”, los casos de represión en protestas y los reiterados escándalos internos. De enero a agosto de 2025, cerca de 1.000 efectivos fueron detenidos por delitos como violencia de género, corrupción y crímenes contra la vida, lo que profundiza la crisis institucional.
                </p>
                <div class="detalle-noticia-image-container-123">
                    <img src="https://backend-zarel.onrender.com/static/img/noticias/peru/noticia4.png" alt="Imagen relacionada" class="detalle-noticia-image-content-123" />
                </div> 
               <p>
                  El exdirector de la PNP, Eduardo Pérez Rocha, considera que los constantes casos de corrupción y la falta de protección efectiva al ciudadano son factores que erosionan la confianza pública. Según explicó, muchas víctimas de extorsión desconfían en denunciar porque los delincuentes obtienen información desde las propias comisarías. Para los analistas, la única forma de revertir la percepción negativa es con resultados visibles en la lucha contra la delincuencia, una depuración interna rigurosa y un cambio estructural que devuelva el prestigio a una institución clave para la seguridad del país.
                </p>
                """.strip(),
                estado=True
            ),
            OBJCategoria(
                id=3,
                titulo='Senamhi emite alerta naranja: Lima y 16 regiones afrontarán temperaturas de hasta 33 °C y alta radiación UV',
                url=base_url_peru + "noticia5.png",
                fecha="2025-10-24",
                hora="16:42",
                descripcion = """
                <ul>
                <li><b>El Senamhi declaró alerta naranja por el incremento de temperaturas “de moderada a fuerte intensidad” en Lima y otras 16 regiones del país.</b></li>
                <li><b>Las máximas oscilarán entre 25 °C y 33 °C, acompañadas de radiación ultravioleta elevada y ráfagas de viento de hasta 45 km/h.</b></li>
                <li><b>La alerta estará vigente hasta el 25 de octubre, con especial atención en las zonas de sierra y costa sur.</b></li>
                </ul>
                <p>
                  El Servicio Nacional de Meteorología e Hidrología (Senamhi) emitió una alerta naranja por el incremento de temperaturas que afectará a Lima y 16 regiones del país, con valores que podrían llegar hasta los 33 °C. Según el organismo, este fenómeno estará acompañado por un aumento significativo en la radiación ultravioleta y una reducción de la nubosidad hacia el mediodía, lo que intensificará la exposición solar. Además, se prevén ráfagas de viento cercanas a los 45 km/h durante las tardes, especialmente en las zonas costeras y altoandinas.
                </p>
                <div class="detalle-noticia-image-container-123">
                    <img src="https://backend-zarel.onrender.com/static/img/noticias/peru/noticia6.png" alt="Imagen relacionada" class="detalle-noticia-image-content-123" />
                </div> 
               <p>
                 La medida, vigente hasta la medianoche del 25 de octubre, incluye regiones como Áncash, Arequipa, Cusco, Piura y Tacna. El Senamhi recomendó a la población tomar precauciones frente a la radiación UV, mantenerse hidratada y evitar la exposición prolongada al sol en horas pico. Las proyecciones climáticas apuntan a un fin de semana de primavera inusualmente cálida, con temperaturas por encima del promedio habitual, reflejando los efectos de la variabilidad climática que atraviesa gran parte del país.
                </p>
                """.strip(),
                estado=True
            )
        ]
    }




















    categoria_nombre = categoria   # ✅ Solo usar el string directo

    return datos.get(categoria_nombre, [])   # ✅ Esto está bien



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

        # Crear el cliente del nuevo SDK
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


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
            return "Lo siento, no puedo responder a esa consulta en este momento. ¿Puedo ayudarte con información sobre Radio Luminares?"
    except Exception as e:
            return "Disculpa, no pude generar una respuesta. ¿Te interesa conocer algo sobre Radio Luminares?"


