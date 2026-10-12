import random 
import re

class ChatbotPeliculas:
    def __init__(self, nombre="ELIZA"):
        self.nombre = nombre
        self.historial_peliculas = set()
        self.reflejos = {
            "yo": "tú", "mi": "tu", "mis": "tus", "me": "te",
            "soy": "eres", "estoy": "estás", "quiero": "quieres",
            "tengo": "tienes", "tu": "mi", "tus": "mis", "vi": "viste",
            "fui": "fuiste", "me gusta": "te gusta"
        }
        
        # Las reglas van de la más específica a la más general
        self.reglas = [
            (r".*\b(recomienda|recomiéndame|recomendar)\b.*", [
                "¡Claro! ¿Qué género te apetece ver hoy: terror, comedia o acción?",
                "Te recomiendo ver un clásico. ¿Prefieres algo de suspenso o prefieres reírte?"
            ]),
            (r".*\b(terror|miedo|horror)\b.*", [
                "¡Qué valor! Te recomiendo 'El Conjuro' o 'Hereditary'. ¿Te gustan las de fantasmas o gore?",
                "El cine de terror es genial. ¿Has visto 'Psicosis' de Alfred Hitchcock?"
            ]),
            (r".*\b(comedia|graciosa|risa)\b.*", [
                "Para reír un buen rato te sugiero '¿Qué pasó ayer?' o 'Superbad'.",
                "¡Excelente elección! Las de comedia nunca fallan. ¿Te gustan las comedias románticas?"
            ]),
            (r".*\b(accion|acción|disparos|peleas)\b.*", [
                "¡Adrenalina pura! Tienes que ver 'John Wick' o 'Mad Max: Fury Road'.",
                "Las de acción son mis favoritas. ¿Prefieres persecuciones de autos o superhéroes?"
            ]),
            (r"(.*)", [
                "¡Qué interesante! Cuéntame más sobre tus gustos en el cine.",
                "No estoy seguro de entender, ¿cuál es tu película favorita de todos los tiempos?",
                "¿Prefieres ver películas en el cine o desde la comodidad de tu casa?"
            ])
        ]

    def __str__(self):
         return f"{self.nombre} ({len(self.reglas)} reglas)"   

    def reflejar(self, fragmento):
        """Intercambia los pronombres si la regla captura grupos de texto."""
        if not fragmento:
            return ""
        palabras = fragmento.lower().split()
        return ' '.join(self.reflejos.get(p, p) for p in palabras)

    def responder(self, texto):
        """Busca una coincidencia con las reglas y devuelve una respuesta aleatoria."""
        texto_limpio = texto.lower().strip(".,!? ¿¡")
        
        for patron, respuestas in self.reglas:
            match = re.match(patron, texto_limpio, re.IGNORECASE)
            if match:
                respuesta = random.choice(respuestas)
                # Si la respuesta necesita rellenar campos con los grupos capturados de la regex
                if match.groups() and "{0}" in respuesta:
                    grupos = [self.reflejar(g) for g in match.groups()]
                    return respuesta.format(*grupos)
                return respuesta
                
        return "Cuéntame más sobre tus gustos en el cine."

# --- Ejemplo de Uso ---
if __name__ == "__main__":
    bot = ChatbotPeliculas()
    print(f"--- {bot} Inicializado ---")
    print("Escribe 'salir' para terminar el chat.\n")
    
    while True:
        usuario = input("Tú: ")
        if usuario.lower() == "salir":
            break
        print(f"{bot.nombre}: {bot.responder(usuario)}")
