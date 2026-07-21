from reactpy import component, html

@component
def Me():
    yo = html.div(
        {
            "style": {
                "width": "100%",
                "display": "flex",
                "flex-direction": "column",
                "align-items": "center",
                "justify-content": "center",
            }
        },
        html.style(
            """
            @media (max-width: 1000px) {
                .img-upper {
                    order: -1;
                }
                .seccion-container {
                    flex-direction: column;
                }
                .parrafo{
                    padding: 1rem;
                    text-align: center;
                }
            }
            """
        ),
        html.h2(
            {
                "style": {
                    "padding": "0 0 20px 0",
                    "width": "fit-content"
                }
            },
            "About Me"
        ),
        html.div(
            {
                "class_name": "seccion-container",
                "style": {
                    "display": "flex",
                    "align-items": "center",
                    "justify-content": "center",
                }
            },
            html.div(
                {
                    
                },
                html.p(
                    {
                        "class_name": "parrafo",
                        "style": {
                            "font-size": "0.9rem",
                            "max-width": "700px",
                        }
                    },
                    "Cuando somos niños, vemos una caja de cartón y sabemos que puede ser cualquier cosa. Los adultos suelen ver... bueno, solo una caja de cartón. Yo decidí quedarme con la idea del niño. Siempre he tenido esa curiosidad terca de ver más allá del dibujo del sombrero para descubrir si adentro hay una serpiente, o en mi caso, para entender exactamente cómo está construido todo por dentro.\n\nY tú que estás leyendo esto, ¿qué ves cuando miras las cosas que usas a diario? ¿Te quedas solo con el resultado final, o alguna vez te preguntas cómo funcionan?"
                )
            ),
            html.div(
                {
                    "class_name": "img-upper",
                    "style": {
                        "max-width": "200px",
                        "min-width": "100px",
                        "height": "auto",
                    }
                },
                html.img(
                    {
                        "src": "/static/img/caja.png",
                        "style": {
                            "width": "100%",
                        }
                    }
                )
            ),
        ),
        
        html.div(
            {
                "class_name": "seccion-container",
                "style": {
                    "display": "flex",
                    "align-items": "center",
                    "justify-content": "center",
                }
            },
            html.div(
                {
                    "style": {
                        "max-width": "200px",
                        "min-width": "100px",
                        "height": "auto",
                    }
                },
                html.img(
                    {
                        "src": "/static/img/bombillo.png",
                        "style": {
                            "width": "100%",
                        }
                    }
                )
            ),
            html.div(
                {
                    
                },
                html.p(
                    {
                        "class_name": "parrafo",
                        "style": {
                            "font-size": "0.9rem",
                            "max-width": "700px",
                        }
                    },
                    "Soy Santiago, estudiante de ingeniería en sistemas, pero en el fondo solo soy una persona con el sueño intacto de saber cómo se hacen las cosas. Ese impulso de desarmar y entender es lo que me trajo hasta aquí. Un día puedo estar levantando el backend de una aplicación en Python o programando componentes, otro día estoy organizando capas de ilustración vectorial, y al siguiente, estoy modificando el hardware de una consola o armando un control arcade mecánico desde cero."
                )
            )
        ),
        
        html.div(
            {
                "class_name": "seccion-container",
                "style": {
                    "display": "flex",
                    "align-items": "center",
                    "justify-content": "center",
                    "padding": "0 0 1rem 0",
                }
            },
            html.div(
                {
                    
                },
                html.p(
                    {
                        "class_name": "parrafo",
                        "style": {
                            "font-size": "0.9rem",
                            "max-width": "700px",
                        }
                    },
                    'En un libro muy famoso dicen que "lo esencial es invisible a los ojos". Para la mayoría de la gente, lo que pasa detrás de una pantalla es invisible. Pero para los que creamos, diseñamos y programamos, lo esencial es justamente eso: la lógica, el código, los circuitos y los píxeles que hacen que todo funcione.\n\nNo me conformo con usar la tecnología, me gusta construirla, romperla y volverla a armar. Bienvenido a mi portafolio; ojalá lo que veas aquí despierte un poco tu curiosidad también.'
                )
            ),
            html.div(
                {
                    "class_name": "img-upper",
                    "style": {
                        "max-width": "200px",
                        "min-width": "100px",
                        "height": "auto",
                    }
                },
                html.img(
                    {
                        "src": "/static/img/principito.png",
                        "style": {
                            "width": "100%",
                        }
                    }
                )
            ),
        ),
    )
    
    return yo