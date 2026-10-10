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
    def __str__ (self):
         return f"{self.nombre} ({len(self.reglas)}reglas)"   


def reflejar(self, fragmento):
    palabras=fragmento.lower().split()
    return ' '.join(self.reflejos.get(p,p) for p in palabras)

def responder(self, texto):
    texto=texto.lower().strip(".,!? ¿¡")
    for (patron,respuestas) in self.reglas:
        coincidencia=re.search(patron,texto)
        if coincidencia:
            grupos=[self.reflejar(g) for g in coincidencia.groups()]
            return random.choice(respuestas).format(*grupos)
        return "No entendi, ¿me lo repites?"