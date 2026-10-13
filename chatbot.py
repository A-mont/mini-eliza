import re

class Chatbot:
    def __init__(self):
        # Estructura de reglas: (patrón_regex, [lista_de_respuestas])
        self.reglas = [
            (
                r"hola|buenos dias|buenas tardes", 
                [
                    "Hola, ¿cómo estás hoy?", 
                    "Hola, ¿de qué te gustaría hablar?"
                ]
            ),
            (
                r"me siento (.*)", 
                [
                    "¿Por qué te sientes {}?", 
                    "¿Qué crees que te hace sentir {}?", 
                    "¿Te pasa seguido que te sientes {}?"
                ]
            ),
            (
                r"mi (.*) es (.*)", 
                [
                    "¿Por qué crees que tu {} es {}?", 
                    "Hablemos más de tu {}."
                ]
            ),
            (
                r"tengo miedo de (.*)", 
                [
                    "¿Qué es lo que más te asusta de {}?", 
                    "¿Por qué te da miedo {}?"
                ]
            ),
            (
                r"(.*) madre (.*)|(.*) padre (.*)",
                [
                    "Cuéntame más sobre tu familia.",
                    "¿Cómo es la relación con tus padres?"
                ]
            )
        ]
