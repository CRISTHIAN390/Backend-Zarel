from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import os
# Tus cruds
from cruds import informacion, patrocinador, catalogo, informacion2

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Inicializar la aplicación Flask
app = FastAPI()


# Configurar CORS para produccion caso contrario : http://localhost:3000
#CORS(app, resources={r"/*": {"origins": "https://paginazareli.onrender.com"}})
# CORS (para desarrollo permitir *)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -------------------------------------------------------------------
# SERVIR ARCHIVOS ESTÁTICOS
# -------------------------------------------------------------------

@app.get("/static/img/noticias/mundo/{filename}")
def imagen_mundo(filename: str):
    return FileResponse(f"img/noticias/mundo/{filename}")

@app.get("/static/img/noticias/peru/{filename}")
def imagen_peru(filename: str):
    return FileResponse(f"img/noticias/peru/{filename}")

@app.get("/static/img/patrocinadores/{filename}")
def imagen_patro(filename: str):
    return FileResponse(f"img/patrocinadores/{filename}")

@app.get("/static/img/catalogo/{filename}")
def imagen_catalogo(filename: str):
    return FileResponse(f"img/catalogo/{filename}")

@app.get("/static/audio/{filename}")
def audio(filename: str):
    return FileResponse(f"audio/{filename}")

#---------------
# 🔹 2. Callback: Mercado Pago redirige aquí con ?code=...
@app.get("/oauth/mercadopago/callback")
async def mercadopago_callback(request: Request):

    # Obtener el code enviado por Mercado Pago en la URL
    code = request.query_params.get("code")

    if not code:
        return JSONResponse(
            status_code=400,
            content={"error": "Código de autorización no recibido"}
        )

    # Aquí NO llamas aún a token_url, igual que tu versión Flask.
    token_url = "https://api.mercadopago.com/oauth/token"

    return {
        "message": "Cuenta conectada exitosamente ✅",
        "mercado_pago_data": code
    }





# -------------------------------------------------------------------
# RUTAS BÁSICAS
# -------------------------------------------------------------------
@app.get("/")
def home():
    return {"message": "API operativa correctamente."}

# Ruta para enviar el enlace
@app.get("/emisora")
def emisora():
    enlacempc = "https://s6.myradiostream.com/49872/listen.mp3"
    #https://playerservices.streamtheworld.com/api/livestream-redirect/CRP_MOD.mp3"
    return {"url": enlacempc}

# Ruta para televisión en vivo
@app.get("/television")
def television():
    # Aquí puedes cambiar la URL dinámicamente si quieres  #?autoplay=1&mute=0
    #https://www.youtube.com/embed/Y-IlMeCCtIg?autoplay=1&mute=0
    #https://www.youtube.com/embed/7b3GhFqWPsc?autoplay=1&mute=0
    #https://www.youtube.com/embed/Nkrl3cfaqKg?autoplay=1&mute=0
    #https://iframe.dacast.com/live/c2386b04-15aa-974b-6912-f8fd63cd782a/94e4c98b-d4d3-8584-2d0c-3338128283ba
    #https://player.twitch.tv/?channel=lumin778&parent=localhost
    stream_url = 'https://player.twitch.tv/?channel=lumin778&parent=localhost'
    return {"stream_url": stream_url}


# Tu endpoint POST
@app.post("/api/informacion")
def obtener_informacion(categoria: str):
  
    print("JSON recibido:", categoria.dict())

    # Llamar a tu CRUD igual que antes
    resultado = informacion.obtener_informacion(categoria)

    # Serializar objetos igual que en Flask
    resultado_serializado = [obj.__dict__ for obj in resultado]

    return JSONResponse(content=resultado_serializado)

@app.get("/api/patrocinadores")
def get_patrocinadores():
    datos = patrocinador.obtener_lista()
    return datos

@app.get("/api/catalogo")
def get_catalogos():
    return catalogo.obtener_listac()

@app.get("/api/catalogo/enlace")
def get_catalogosurl():
    return {"enlace_url": "https://www.youtube.com/embed/Nkrl3cfaqKg?autoplay=1&mute=0"}


# ============================================
#  CHATBOT
# ============================================
class Datax(BaseModel):
    mensaje: str

@app.post("/api/geminix")
async def asistentechatbot(data: Datax):
    try:
        respuesta = informacion.asistentechatbot(data.mensaje)
        return {"respuesta": respuesta}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/geminix2")
async def asistentechatbot2(data: Datax):
    try:
        respuesta = informacion2.asistentechatbot2(data.mensaje)
        return {"respuesta": respuesta}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/consuldoc")
def consuldoc(data: dict):
    try:
        respuesta = informacion.procesarInfo(data)
        return respuesta
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# -------------------------------------------------------------------
# MANEJO DE RUTAS NO EXISTENTES
# -------------------------------------------------------------------
@app.exception_handler(404)
async def not_found(request, exc):
    return JSONResponse(
        status_code=404,
        content={"message": "Ruta no encontrada. Verifica la URL."}
    )

# -------------------------------------------------------------------
# MODO DESARROLLO LOCAL (Uvicorn)
# -------------------------------------------------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
         #  "main:app",
        host="127.0.0.1",
        port=4500,
        reload=True
    )

#uvicorn main:app --reload --host 127.0.0.1 --port 4500

#gunicorn main:app \-w 4 \ -k uvicorn.workers.UvicornWorker \ --bind 0.0.0.0:4500
