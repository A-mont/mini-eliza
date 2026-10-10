import random 
import re

class Chatbot:

    def __init__(self, nombre="Eliza"):
        self.nombre = nombre
        self.reflejos={
            "yo": "tú","mi": "tu", "mis": "tus", "me": "te", 
            "soy": "eres", "estoy": "estás","quiero": "quieres", 
            "tengo": "tienes", "tu":"mi","tus":"mis",
        } 
        self.reglas=[]
    def__str__(self):
  return f"{self.nombre}({len(self.reglas)}reglas)"   
            