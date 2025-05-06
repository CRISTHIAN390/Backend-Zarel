from pydantic import BaseModel

class CategoriaRequest(BaseModel):
    categoria: str

class OBJCategoria(BaseModel):
    id: int
    titulo: str
    url: str    # aquí irá la ruta de la imagen
    fecha: str
    hora: str
    descripcion: str
    estado: bool
    
