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


    def reflejar(self, fragmento):
        #Cambia la persona gramatical: ´mi juego´ -> ´tu juego´
        palabras= fragmento.lower().split()
        return " ".join([self.reflejos.get(p, p) for p in palabras])

    def responder(self, texto):
        #Devuelve la respuesta de la primera regla que coincida.
        texto = texto.lower().strip(" .,!?¡¿")
        for patron, respuestas in self.reglas:
            coincidencia = re.match(patron, texto)
            if coincidencia:
                grupos = [self.reflejar(g) for g in coincidencia.groups()]
                return random.choice(respuestas).format(*grupos)
        return "No entiendí, ¿me lo repites?"