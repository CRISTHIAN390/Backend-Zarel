from pydantic import BaseModel

class OBJCategoria(BaseModel):
    id: int
    titulo: str
    url: str    # aquí irá la ruta de la imagen
    fecha: str
    hora: str
    descripcion: str
    estado: bool
    
