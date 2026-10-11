import re
import random

class Chatbot:
    def __init__(self, nombre="ELIZA"):
        self.nombre = nombre
        self.nombre_usuario = None
        self.historial_peliculas = set()  # <-- Nuevo: Almacena películas únicas mencionadas
        self.reflejos = {
            "yo": "tú", "mi": "tu", "mis": "tus", "me": "te",
            "soy": "eres", "estoy": "estás", "quiero": "quieres",
            "tengo": "tienes", "tu": "mi", "tus": "mis", "vi": "viste",
            "fui": "fuiste", "me gusta": "te gusta"
        }
        self.reglas = []

    def __str__(self):
        return f"{self.nombre} ({len(self.reglas)} reglas)"

    def reflejar(self, fragmento):
        palabras = fragmento.lower().split()
        palabras_reflejadas = [self.reflejos.get(p, p) for p in palabras]
        return " ".join(palabras_reflejadas)

    def responder(self, mensaje):
        mensaje = mensaje.strip().lower()
        
        for patron, respuestas in self.reglas:
            match = re.match(patron, mensaje, re.IGNORECASE)
            if match:
                respuesta = random.choice(respuestas)
                
                # --- VALIDACIÓN DE NOMBRE ---
                if "nombre" in patron or "soy " in patron:
                    if match.groups():
                        posible_nombre = match.group(1).strip()
                        # Si tiene 2 palabras o menos, lo aceptamos como un nombre válido
                        if len(posible_nombre.split()) <= 2:
                            self.nombre_usuario = posible_nombre.capitalize()
                        else:
                            # Si es una frase larga, sobreescribimos la respuesta del bot
                            return "Eso suena a una frase muy larga. ¿Podrías decirme solo tu nombre de pila?"
                
                # --- CAPTURA DE HISTORIAL DE PELÍCULAS ---
                if "película" in patron or "pelicula" in patron:
                    if match.groups() and "%1" in respuesta:
                        # Extraemos el título original (sin reflejar gramática) para el historial
                        titulo_pelicula = match.group(1).strip().title()
                        self.historial_peliculas.add(titulo_pelicula)

                # Reemplazo de fragmentos reflejados (%1)
                if match.groups() and "%1" in respuesta:
                    fragmento_reflejado = self.reflejar(match.group(1))
                    respuesta = respuesta.replace("%1", fragmento_reflejado)
                
                # Reemplazo dinámico del nombre del usuario (%usuario)
                if "%usuario" in respuesta:
                    if self.nombre_usuario:
                        respuesta = respuesta.replace("%usuario", self.nombre_usuario)
                    else:
                        respuesta = respuesta.replace("%usuario", "amigo cinéfilo")
                        
                return respuesta
                
        # Respuesta por defecto si no hay coincidencia
        if self.nombre_usuario:
            return f"Cuéntame más sobre tus gustos en el cine, {self.nombre_usuario}."
        return "Cuéntame más sobre tus gustos en el cine."
