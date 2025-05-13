from pydantic import BaseModel

class OBJPatro(BaseModel):
    id: int
    nombre: str
    imagen: str    # aquí irá la ruta de la imagen
    descripcion: str
    url: str       # aquí irá la url de su pagina web
    telefono: str
    estado: bool
    
