from models.catalogo import OBJCatalogo

def obtener_listac():
    base_url = "https://backend-zarel-production.up.railway.app/static/img/catalogo/"
    datoss = [
        {
            "id": 1,
            "nombre": "Ruben Diaz y Esposa | Medley de alabanzas |",
            "imagen": base_url + "imagencat.png",
            "fecha": "25/03/2025",
            "descripcion": "Fue un privilegio tenerlos en la celebración de nuestro 51 aniversario",
            "videoId": "5a_B4Vstu-k",
            "estado": True
        },
        {
            "id": 2,
            "nombre": "CICATRICES, MARCAS DE HONOR | Pr. Ever Marquez",
            "imagen": base_url + "imagencat.png",
            "fecha": "14/03/2025",
            "descripcion": "Dialogo sobre acontecimientos de la vida y la sociedad",
            "videoId": "vJeBoTqllNs",
            "estado": True
        },
        {
            "id": 3,
            "nombre": "BENDITA HONRA | Pr Ever Marquez | ",
            "imagen": base_url + "imagencat.png",
            "fecha": "12/10/2024",
            "url": "Bablemos sobre la Bendita Honra y el Espiritu Santo",
            "videoId": "kgzmRtfcFSc",
            "estado": True
        },
                {
            "id": 4,
            "nombre": "Pr. Ever Marquez #8 | La voluntad de Dios ",
            "imagen": base_url + "imagencat.png",
            "fecha": "4/09/2024",
            "url": "Dialogo sobre acontecimientos de la vida y la voluntad de Dios",
            "videoId": "kgzmRtfcFSc",
            "estado": True
        },

    ]
    return datoss


