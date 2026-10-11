"""Chatbot temático de películas y recomendaciones de cine."""
from chatbot import Chatbot

class ChatbotPeliculas(Chatbot):
    """Crítico y recomendador de cine virtual."""
    
    def __init__(self):
        """Define el nombre del bot y sus reglas específicas de conversación."""
        super().__init__("CineBot")
        self.reglas = [
            (r"\b(?:hola|buen[oa]s)\b",
             ["¡Hola cinéfilo! ¿De qué película o género te gustaría hablar hoy?"]),
            
            (r"no me gusta la pel[ií]cula (.*)",
             ["¿Por qué no te gustó {0}? ¿Fue por el final o los actores?",
              "Vaya, {0} suele dividir opiniones. ¿Qué le cambiarías?"]),
            
            (r"me gusta la pel[ií]cula (.*)",
             ["¡Buenísima elección! ¿Qué es lo que más rescatas de {0}?",
              "¿Cuántas veces has visto {0}? Es un clásico moderno."]),
            
            (r"quiero ver una de (.*)",
             ["Si buscas de {0}, te sugiero revisar las más premiadas.",
              "¡Excelente plan! ¿Prefieres un estreno de {0} o algo clásico?"]),
            
            (r"cu[aá]nto cuesta|precio|boleto",
             ["Los boletos digitales están en $85 pesos y los miércoles hay 2x1."]),
            
            (r"recomienda|sugiere",
             ["Te recomiendo ver 'Interstellar' si te gusta la ciencia ficción o 'Parasite' para algo de suspenso."]),
            
            (r"(.*)",
             ["¿Qué actores o directores te gustan de {0}?",
              "Cuéntame más sobre tu relación con el cine.",
              "¿Prefieres ver {0} en el cine o desde la comodidad de tu casa?"])
        ]
