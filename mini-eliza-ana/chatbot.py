
"""clase base para un chatbot al estilo eliza"""
import random
import re
class chatbot:
    """chatbot que responde con reglas de patron y plantillas"""
def __init__(self,nombre="eliza"):
   self.nombre=nombre
   self.reflejos = {
       
    "yo":"tu","mi":"tu","mis" "yo": "tú", "mi": "tu", "mis": "tus", "me": "te", "soy": "eres", "estoy": "estás", "quiero": "quieres", "tengo": "tienes", "tu": "mi", "tus": "mis",
}

   self.reglas = []


   def __str__(self):
    return f"{self.nombre} ({len(self.reglas)} reglas)"