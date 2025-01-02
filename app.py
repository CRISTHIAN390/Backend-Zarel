from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)
CORS(app)

# Configuración de Flask-Mail
app.config['MAIL_SERVER'] = 'sandbox.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

# Ruta vacía para verificar que el servidor funciona
@app.route('/')
def home():
    return "Bienvenido a la API de Flask Mail. Todo funciona correctamente."

# Ruta para enviar correos
@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.get_json()
    nombre = data.get('nombre')
    correo = data.get('correo')
    descripcion = data.get('descripcion')

    if not all([nombre, correo, descripcion]):
        return jsonify({"message": "Todos los campos son obligatorios"}), 400

    msg = Message(
        subject=f"Consulta recibida de {nombre}",
        sender="no-reply@example.com",
        recipients=[correo],
        body=f"Hola {nombre},\n\nHemos recibido tu consulta:\n{descripcion}\n\nGracias por contactarnos."
    )
    mail.send(msg)
    return jsonify({"message": "Correo enviado con éxito"}), 200

# Manejo de error 404
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"message": "Ruta no encontrada. Verifica la URL."}), 404

if __name__ == '__main__':
    app.run(debug=True)
