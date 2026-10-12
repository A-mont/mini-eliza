"""Chatbot temático de música."""
import re
from chatbot import Chatbot

class ChatbotMusica(Chatbot):
    """Asistente virtual que conversa sobre música."""

    def __init__(self):
        super().__init__("Melody")
        self.reglas = [
            (r"\b(?:hola|buenos días|buenas tardes|buenas noches)\b",
             ["¡Hola! Bienvenido al mundo de la música. ¿Qué tipo de música te gusta?"]),

            (r"no me gusta (.*)",
             ["¿Por qué no te gusta {0}? ¿Qué género prefieres?"]),

            (r"me gusta (.*)",
             ["¡Qué bien! ¿Qué es lo que más disfrutas de {0}?"]),

            (r"quiero escuchar (.*)",
             ["¡Buena elección! Espero que disfrutes escuchar {0}.",
              "¿Qué otra canción de {0} te gusta?"]),

            (r"mi cantante favorito es (.*)",
             ["¡Genial! ¿Cuál es tu canción favorita de {0}?"]),

            (r"recomienda",
             ["Te recomiendo escuchar pop, rock o música instrumental. ¿Qué género prefieres?"]),

            (r"canciones tristes",
             ["Las canciones tristes pueden ayudarte a expresar tus emociones. ¿Cuál es tu favorita?"]),

            (r"adiós|hasta luego",
             ["¡Hasta pronto! Que nunca te falte la música."]),

            (r"(.*)",
             ["Cuéntame más sobre tus gustos musicales.",
              "¿Qué artista te gusta escuchar?",
              "¿Cuál es tu canción favorita?"]),
        ]