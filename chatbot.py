import re

class Chatbot:
    def __init__(self):
        # Estructura de reglas adaptada al CineBot: (patrón_regex, [lista_de_respuestas])
        self.reglas = [
            (
                r"\b(?:hola|buen[oa]s)\b",
                [
                    "¡Hola! Bienvenido al mundo del cine. ¿Qué película te gustaría comentar?",
                    "¡Hola! Soy CineBot. ¿De qué película o género quieres hablar hoy?"
                ]
            ),
            (
                r"me gusta (.*)",
                [
                    "¡Qué bien! A mí también me interesa {}. ¿Qué es lo que más te gusta de esa película?",
                    "Interesante. ¿Qué otras películas parecidas a {} has visto?"
                ]
            ),
            (
                r"no me gusta (.*)",
                [
                    "Entiendo que no te guste {}. ¿Qué otra película prefieres?",
                    "¿Qué es lo que menos te convenció de {}?"
                ]
            ),
            (
                r"quiero ver (.*)",
                [
                    "¡Buena elección! {} podría ser una excelente opción.",
                    "¿Qué te motivó a querer ver {}?"
                ]
            ),
            (
                r"mi película favorita es (.*)",
                [
                    "¡{} suena increíble! ¿Qué es lo que más te apasiona de ella?",
                    "Es un clásico. ¿Cuántas veces has visto {}?"
                ]
            ),
            (
                r"recomienda|recomiéndame",
                [
                    "Te recomiendo ver una película de aventura, comedia o ciencia ficción. ¿Qué género prefieres?",
                    "Si buscas algo bueno, el cine de suspenso o drama nunca falla. ¿Te llama la atención alguno?"
                ]
            ),
            (
                r"género|genero",
                [
                    "Hay muchos géneros fascinantes: acción, comedia, terror, romance, aventura y ciencia ficción.",
                    "A mí me gustan todos los géneros, pero el suspenso es especial. ¿Cuál es tu favorito?"
                ]
            ),
            (
                r"cuánto dura|cuanto dura|duración|duracion",
                [
                    "La duración depende de la película. Hay películas de menos de 90 minutos y otras que duran más de dos horas."
                ]
            ),
            (
                r"(.*)",
                [
                    "Cuéntame más sobre esa película.",
                    "¿Qué otra película te gusta?",
                    "Interesante. ¿Qué opinas de esa película?"
                ]
            )
        ]
