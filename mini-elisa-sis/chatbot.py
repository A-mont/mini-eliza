"""Clase base para un chatbot al estilo ELISA."""
import random 
import re 

class Chatbot:
"""Chatbot que responde con reglas de patrón y plantillas."""
    def __init__(self, nombre="ELISA"):
        self.nombre = nombre 
        self.reflejo = {
            "yo": "tú", "mi": "tu", "mis": "tus", "me": "te",
            "soy": "eres", "estoy": "estás", "quiero": "quieres",
            "tengo": "tienes", "tu": "mi", "tus": "mis",
        }
        self.reglas = []
    def __str__(self):
        return f"{self.nombre} ({len(self. reglas)} reglas)"