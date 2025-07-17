from models.patrocinador import OBJPatro

def obtener_lista():
    base_url = "https://backend-zarel-production.up.railway.app/static/img/patrocinadores/"
    datos = [
        {
            "id": 1,
            "nombre": "Ferreteria Emanuel SAC",
            "imagen": base_url + "ferreteria.jpg",
            "descripcion": "En nuestra distribuidora, ofrecemos una amplia variedad de productos para construcción y remodelación, enfocados en satisfacer tanto a clientes mayoristas como minoristas. Nos esforzamos en brindar materiales de alta calidad y un servicio eficiente para apoyar tus proyectos.",
            "url": "https://grupoemanuelrlg.com//emanuel/proferreteria",
            "telefono": "999999999",
            "estado": True
        },
        {
            "id": 2,
            "nombre": "Hotel Emanuel",
            "imagen": base_url + "hotel.jpg",
            "descripcion": "En nuestro hotel, ofrecemos un espacio acogedor y multifuncional para garantizar una estancia placentera. Nos especializamos en el hospedaje cómodo y seguro, así como en la renta de instalaciones para eventos.",
            "url": "https://grupoemanuelrlg.com/emanuel/hotel",
            "telefono": "999999999",
            "estado": True
        },
        {
            "id": 3,
            "nombre": "Servicentro Emanuel",
            "imagen": base_url + "servicentro.jpg",
            "descripcion": "En Servicentro Emanuel, nos especializamos en el cuidado y mantenimiento de vehículos de transporte, tanto livianos como pesados. Ofrecemos una gama completa de servicios para garantizar que tu vehículo esté siempre en óptimas condiciones.",
            "url": "https://grupoemanuelrlg.com/emanuel/servicentro",
            "telefono": "999999999",
            "estado": True
        },
                {
            "id": 4,
            "nombre": "Complejo deportivo triple G",
            "imagen": base_url + "tripleg.jpg",
            "descripcion": "En nuestro complejo deportivo, brindamos una experiencia única y accesible para deportistas de todas las edades. Ofrecemos instalaciones modernas y seguras, equipadas con la mejor tecnología y diseñadas para crear un ambiente donde los jóvenes y aficionados puedan disfrutar plenamente de sus actividades deportivas favoritas.",
            "url": "https://grupoemanuelrlg.com/emanuel/complejo",
            "telefono": "999999999",
            "estado": True
        },
                        {
            "id": 5,
            "nombre": "Servicios Generales G & Z SAC",
            "imagen": base_url + "zareli.jpg",
            "descripcion": "En Servicios Generales G & Z SAC, nos dedicamos a la distribución de una extensa gama de productos para construcción y remodelación. Atendemos tanto a clientes mayoristas como minoristas, ofreciendo materiales de primera calidad y un servicio ágil y comprometido con el éxito de tus proyectos.",
            "url": "https://paginazareli.onrender.com",
            "telefono": "999999999",
            "estado": True
        },
                                {
            "id": 6,
            "nombre": "Vidal Tech Solutions",
            "imagen": base_url + "criss.jpg",
            "descripcion": "Somos una empresa especializada en soluciones tecnológicas y asesoría contable, enfocada en el desarrollo de software, aplicaciones móviles y sistemas de gestión administrativa, entre otros. Combinamos innovación, experiencia y compromiso para brindar herramientas digitales que optimicen procesos y potencien el crecimiento de nuestros clientes.",
            "url": "",
            "telefono": "999999999",
            "estado": True
        },
        #https://cvidal.onrender.com/#perfil

    ]
    return datos

