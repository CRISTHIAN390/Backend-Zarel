from models.informacion import OBJCategoria

def obtener_informacion(categoria: str):
    base_url = "https://backend-zarel.onrender.com/static/img/"

    datos = {
        "Mundo": [
            OBJCategoria(
                id=1,
                titulo="Noticia Mundial 1",
                url=base_url + "tele.png",
                fecha="2025-05-06",
                hora="14:30",
                descripcion="Descripción de la noticia mundial 1",
                estado=True
            ),
            OBJCategoria(
                id=2,
                titulo="Noticia Mundial 2",
                url=base_url + "apoyo.png",
                fecha="2025-05-06",
                hora="16:45",
                descripcion="Descripción de la noticia mundial 2",
                estado=True
            )
        ],
        "Peru": [
            OBJCategoria(
                id=1,
                titulo="Noticia Perú 1",
                url=base_url + "extra.png",
                fecha="2025-05-06",
                hora="09:15",
                descripcion="Descripción de la noticia Perú 1",
                estado=True
            ),
            OBJCategoria(
                id=2,
                titulo="Noticia Perú 2",
                url=base_url + "tele.png",
                fecha="2025-05-06",
                hora="11:00",
                descripcion="Descripción de la noticia Perú 2",
                estado=True
            )
        ]
    }

    categoria_nombre = categoria   # ✅ Solo usar el string directo

    return datos.get(categoria_nombre, [])   # ✅ Esto está bien
