from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from flask_cors import CORS
from dotenv import load_dotenv
import os
from pydantic import BaseModel
from flask import send_from_directory
from cruds import informacion,patrocinador,catalogo,informacion2
# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Inicializar la aplicación Flask
app = Flask(__name__)
# Montar la carpeta img para servir archivos estáticos

# Ruta para servir imágenes desde la carpeta img
@app.route('/static/img/noticias/mundo/<path:filename>')
def serviri_imagenesmundo(filename):
    return send_from_directory('img/noticias/mundo', filename)

# Ruta para servir imágenes desde la carpeta img/noticias/peru
@app.route('/static/img/noticias/peru/<path:filename>')
def servir_imagenesperu(filename):
    return send_from_directory('img/noticias/peru', filename)

# Ruta para servir imágenes desde la carpeta img/patrocinadores
@app.route('/static/img/patrocinadores/<path:filename>')
def servir_imagenpatro(filename):
    return send_from_directory('img/patrocinadores', filename)

@app.route('/static/img/catalogo/<path:filename>')
def servir_imagencatalog(filename):
    return send_from_directory('img/catalogo', filename)

# Servir audios desde la carpeta /audio
@app.route('/static/audio/<path:filename>')
def serve_audio(filename):
    return send_from_directory('audio', filename)

# Configurar CORS para produccion caso contrario : http://localhost:3000
#CORS(app, resources={r"/*": {"origins": "https://paginazareli.onrender.com"}})
CORS(app)  

# Configuración de Flask-Mail
app.config['MAIL_SERVER'] = 'sandbox.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')  # Usuario desde el archivo .env
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')  # Contraseña desde el archivo .env
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

# Inicializar Flask-Mail
mail = Mail(app)

# Ruta raíz para verificar que el servidor está funcionando
@app.route('/')
def home():
    return "Bienvenido a la API de Flask Mail. Todo funciona correctamente."

# Ruta para enviar el enlace
@app.route('/emisora', methods=['GET'])
def enlace():
    enlacempc = "https://s6.myradiostream.com/49872/listen.mp3"
    #https://playerservices.streamtheworld.com/api/livestream-redirect/CRP_MOD.mp3"
    return jsonify({"url": enlacempc})

@app.route('/television', methods=['GET'])
def get_stream_url():
    # Aquí puedes cambiar la URL dinámicamente si quieres  #?autoplay=1&mute=0
    #https://www.youtube.com/embed/Y-IlMeCCtIg?autoplay=1&mute=0
    #https://www.youtube.com/embed/7b3GhFqWPsc?autoplay=1&mute=0
    #https://www.youtube.com/embed/Nkrl3cfaqKg?autoplay=1&mute=0
    #https://iframe.dacast.com/live/c2386b04-15aa-974b-6912-f8fd63cd782a/94e4c98b-d4d3-8584-2d0c-3338128283ba
    #https://player.twitch.tv/?channel=lumin778&parent=localhost
    stream_url = 'https://player.twitch.tv/?channel=lumin778&parent=localhost'
    return jsonify({'stream_url': stream_url})


# Tu endpoint POST
@app.route('/api/informacion', methods=['POST'])
def obtener_informacion():
    categoria_data = request.get_json()
    print("JSON recibido:", categoria_data)  # Para confirmar lo que llega

    # Asegurarse de extraer la 'categoria'
    categoria = categoria_data.get('categoria')   

    # Validación simple por si acaso
    if not categoria:
        return jsonify({'error': 'No se recibió categoría'}), 400


    resultado = informacion.obtener_informacion(categoria)
    resultado_serializado = [obj.__dict__ for obj in resultado]  
    return jsonify(resultado_serializado)

@app.route('/api/patrocinadores', methods=['GET'])
def get_patrocinadores():
    datos = patrocinador.obtener_lista()
    return jsonify(datos)

@app.route('/api/catalogo', methods=['GET'])
def get_catalogos():
    datoss = catalogo.obtener_listac()
    return jsonify(datoss)

#ENLACE DE YOUTUBE
@app.route('/api/catalogo/enlace', methods=['GET'])
def get_catalogosurl():
    # Aquí puedes cambiar la URL dinámicamente si quieres
    #Noticias: https://www.youtube.com/embed/Y-IlMeCCtIg?autoplay=1&mute=0
    enlace_url = 'https://www.youtube.com/embed/Nkrl3cfaqKg?autoplay=1&mute=0'
    return jsonify({'enlace_url': enlace_url})

# ============================================
#  CHATBOT
# ============================================
class Datax(BaseModel):
    mensaje: str
@app.route('/api/geminix', methods=['POST'])
def asistentechatbot():
    data = request.get_json()
    mensaje = data.get('mensaje', '')
    respuesta = informacion.asistentechatbot(mensaje)
    return jsonify({"respuesta": respuesta})


class Datax(BaseModel):
    mensaje: str
@app.route('/api/geminix2', methods=['POST'])
def asistentechatbot2():
    data = request.get_json()
    mensaje = data.get('mensaje', '')
    respuesta = informacion2.asistentechatbot2(mensaje)
    return jsonify({"respuesta": respuesta})


# Ruta para enviar correos
@app.route('/send-email', methods=['POST'])
def send_email():
    try:
        # Obtener los datos del cliente
        data = request.get_json()
        nombre = data.get('nombre')
        correo = data.get('correo')
        descripcion = data.get('descripcion')
        # Validar los campos
        if not all([nombre, correo, descripcion]):
            return jsonify({"message": "Todos los campos son obligatorios"}), 400
        # Configuración del mensaje de correo
        # Plantilla HTML para el correo
        html_content = f"""
        <html>
        <body>
            <h1 style="color: #000000; font-size: 24px;">Servicios Generales Gabriel & Zareli SAC</h1>
            <h4 style="color: #ff7b00; font-size: 15px;">Consulta Recibida Por</h4>
            <p><strong>Nombre:</strong> {nombre}</p>
            <p><strong>Email:</strong> {correo}</p>
            <p><strong>Mensaje:</strong></p>
            <p>{descripcion}</p>
        </body>
        </html>
        """
        # Configuración del mensaje de correo con HTML
        msg = Message(
            subject="Nueva Consulta Recibida",
            sender="no-reply@example.com",  # Cambiar a un correo válido si es necesario
            recipients=[correo],
            html=html_content  # Enviar el contenido en formato HTML
        )
        # Enviar el correo
        mail.send(msg)
        return jsonify({"message": "Correo enviado con éxito"}), 200

    except Exception as e:
        # Capturar errores y devolver un mensaje adecuado
        return jsonify({"message": "Error al enviar el correo", "error": str(e)}), 500

# Manejo de error 404 para rutas no encontradas
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"message": "Ruta no encontrada. Verifica la URL."}), 404

# Iniciar la aplicación
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Leer el puerto desde las variables de entorno
    app.run(host='0.0.0.0', port=port, debug=False)  # Desactivar debug para producción
