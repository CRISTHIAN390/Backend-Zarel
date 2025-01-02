from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Inicializar la aplicación Flask
app = Flask(__name__)

# Configurar CORS para produccion caso contrario : http://localhost:3000
CORS(app, resources={r"/*": {"origins": "https://paginazareli.onrender.com"}})

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
        msg = Message(
            subject="Nueva Consulta Recibida",
            sender="no-reply@example.com",  # Cambiar a un correo válido si es necesario
            recipients=[correo],
            body=f"""Nueva Consulta Recibida
        Nombre: {nombre}
        Email: {correo}
        Mensaje:
        {descripcion}
        """
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
