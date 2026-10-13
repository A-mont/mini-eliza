"""Chatbot temático sobre películas."""

from chatbot import Chatbot


class ChatbotPeliculas(Chatbot):
    """Chatbot que conversa sobre películas."""

    def __init__(self):
        """Inicializa el chatbot especializado en películas."""
        super().__init__()  # Llama al constructor de la clase base Chatbot

        # Diccionario de reflexión (búsqueda y reemplazo de pronombres/verbos)
        self.reflexiones = {
            "mi": "tu",
            "mio": "tuyo",
            "mia": "tuya",
            "mis": "tus",
            "yo": "tú",
            "estoy": "estás",
            "soy": "eres",
            "tengo": "tienes",
            "me": "te",
            "tu": "mi",
            "tuyo": "mío",
            "tuya": "mía",
            "tus": "mis",
            "tú": "yo",
            "estás": "estoy",
            "eres": "soy",
            "tienes": "tengo",
            "te": "me"
        }

        # Reglas específicas para el bot de películas
        self.reglas = [
            (
                r"\b(?:hola|buen[oa]s)\b",
                [
                    "¡Hola! Bienvenido al mundo del cine. "
                    "¿Qué película te gustaría comentar?"
                ]
            ),
            (
                r"me gusta (.*)",
                [
                    "¡Qué bien! A mí también me interesa {0}. "
                    "¿Qué es lo que más te gusta de esa película?"
                ]
            ),
            (
                r"no me gusta (.*)",
                [
                    "Entiendo que no te guste {0}. "
                    "¿Qué otra película prefieres?"
                ]
            ),
            (
                r"quiero ver (.*)",
                [
                    "¡Buena elección! {0} podría ser una buena opción."
                ]
            ),
            (
                r"mi película favorita es (.*)",
                [
                    "¡{0} suena interesante! "
                    "¿Qué es lo que más te gusta de ella?"
                ]
            ),
            (
                r"recomienda|recomiéndame",
                [
                    "Te recomiendo ver una película de aventura, "
                    "comedia o ciencia ficción. ¿Qué género prefieres?"
                ]
            ),
            (
                r"género|genero",
                [
                    "Hay muchos géneros: acción, comedia, terror, "
                    "romance, aventura y ciencia ficción."
                ]
            ),
            (
                r"cuánto dura|cuanto dura|duración|duracion",
                [
                    "La duración depende de la película. "
                    "Hay películas de menos de 90 minutos y otras "
                    "que duran más de dos horas."
                ]
            ),
            (
                r"(.*)",
                [
                    "Cuéntame más sobre esa película.",
                    "¿Qué otra película te gusta?",
                    "Interesante. ¿Qué opinas de esa película?"
                ]
            ),
        ]
