from models.informacion import OBJCategoria

def obtener_informacion(categoria: str):
    base_url = "https://backend-zarel.onrender.com/static/img/"

    datos = {
        "Mundo": [
            OBJCategoria(
                id=1,
                titulo="Terror en el Jockey Plaza: Clientes fueron encerrados en tiendas mientras autoridades controlaban la emergencia",
                url=base_url + "tele.png",
                fecha="2025-05-07",
                hora="05:30",
                descripcion = """
                <ul>
                <li><b>Los clientes se refugiaron en las diversas tiendas para ponerse a buen resguardo</b></li>
                <li><b>La Policía Nacional del Perú explicó lo sucedido</b></li>
                <li><b>Disparos en el primer piso del establecimiento</b></li>
                </ul>
                <p>
                  Minutos de pánico y terror se vivieron en el centro comercial
                  Jockey Plaza, ubicado en Santiago de Surco, debido 
                  a una supuesta balacera.
                  Ciudadanos se refugiaron en las tiendas del lugar para intentar salvaguardar sus vidas ante la emergencia.
                </p>
                <div class="detalle-noticia-image-container-123">
                    <img src="https://backend-zarel.onrender.com/static/img/tele.png" alt="Imagen relacionada" class="detalle-noticia-image-content-123" />
                </div> 
               <p>
                Según testigos, se escucharon disparos en el primer piso del 
                establecimiento al promediar las 2 de la tarde de este domingo 
                18 de mayo.
                Tras los estruendos de aparentemente un arma de fuego, 
                los clientes corrieron despavoridos. Las autoridades 
                desplagaron el protocolo correspondiente para actuar según 
                lo ocurrido.
                </p>
                """.strip(),
                estado=True
            ),
            OBJCategoria(
                id=2,
                titulo="Cómo se forjó la relación especial entre EE.UU. e Israel y por qué algunos creen que está en peligro",
                url=base_url + "apoyo.png",
                fecha="2025-05-06",
                hora="12:45",
                descripcion="Un momento después, el presentador me preguntó sobre los comentarios que acabábamos de escuchar del presidente de Estados Unidos, Donald Trump. Dije que estábamos atestiguando un cambio fundamental en la posición política de Estados Unidos después de décadas del conflicto palestino-israelí.Era febrero de este año y Trump acababa de mantener conversaciones con el primer ministro de Israel, Benjamin Netanyahu, el primer líder extranjero en ser invitado a la Casa Blanca desde la toma de posesión del mandatario estadounidense.",
                estado=True
            ),
            OBJCategoria(
                id=3,
                titulo="México tiene el alma atada a Latinoamérica, pero el cuerpo encadenado a Norteamérica",
                url=base_url + "extra.png",
                fecha="2025-05-06",
                hora="16:45",
                descripcion="Quizá sea un poco de todo eso, y la pregunta es de especial importancia cuando, por primera vez en más de un siglo, un presidente de Estados Unidos, el país más grande de los tres, que disputa lo que se entiende por el subcontinente. Donald Trump quiere presionar a sus vecinos: someter sus políticas comerciales a su antojo, dictar sus estrategias de seguridad y controlar los límites del subcontinente, como Panamá y Groenlandia.",
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
