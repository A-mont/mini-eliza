#Clase base para el chatbot al estilo Eliza
import random
import re

class Chatbot:
    #Chatbot que responde con reglas de patrón y plantillas.

    def __init__(self, nombre="Eliza"):
        self.nombre = nombre
        self.reflejos ={
            "yo": "tú", "mi":"tú", "mis":"tus", "me":"te",
            "soy": "eres", "estoy": "estás", "quiero": "quieres",
            "tengo": "tienes", "tu": "mi", "tus": "mis",
        }
        self.reglas = []

    def __str__(self):
        return f"{self.nombre} ({len(self.reglas)} reglas)"