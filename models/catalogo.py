from pydantic import BaseModel
class OBJCatalogo(BaseModel):
    id: int
    img: str    # aquí irá la ruta de la imagen
    nombre: str  
    fecha: str
    descripcion: str      
    videoId: str
    estado: bool
    
