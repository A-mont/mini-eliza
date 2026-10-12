
import random
import re
import unicodedata


class ChatbotPeliculas:
    def __init__(self, nombre="ELIZA"):
        self.nombre = nombre
        self.historial_peliculas = set()

        # Reglas de conversación: de la más específica a la más general
        self.reglas = [
            (
                r".*\b(recomienda|recomiéndame|recomendar|recomiendame)\b.*",
                [
                    "¡Claro! ¿Qué género te apetece ver hoy: terror, comedia o acción?",
                    "Te recomiendo un clásico. ¿Prefieres suspenso o quieres reírte?"
                ]
            ),
            (
                r".*\b(terror|miedo|horror)\b.*",
                [
                    "¡Qué valor! Te recomiendo 'El Conjuro' o 'Hereditary'. ¿Prefieres fantasmas o gore?",
                    "El cine de terror es genial. ¿Has visto 'Psicosis', de Alfred Hitchcock?"
                ]
            ),
            (
                r".*\b(comedia|graciosa|risa|divertida)\b.*",
                [
                    "Para reír un buen rato te sugiero '¿Qué pasó ayer?' o 'Superbad'.",
                    "¡Excelente elección! ¿Te gustan las comedias románticas?"
                ]
            ),
            (
                r".*\b(accion|disparos|peleas|aventura)\b.*",
                [
                    "¡Adrenalina pura! Tienes que ver 'John Wick' o 'Mad Max: Fury Road'.",
                    "¿Qué prefieres: persecuciones de autos o películas de superhéroes?"
                ]
            ),
            (
                r".*\b(drama|romance|romantica|romántica)\b.*",
                [
                    "Te recomiendo 'Titanic' si te gusta el romance.",
                    "Si prefieres el drama, puedes ver 'En busca de la felicidad'."
                ]
            ),
            (
                r".*\b(ciencia ficcion|ciencia ficción|espacio|futurista)\b.*",
                [
                    "¡La ciencia ficción es fascinante! Te recomiendo 'Interestelar'.",
                    "Puedes ver 'Matrix' si te gustan las historias futuristas."
                ]
            ),
            (
                r".*\b(hola|buenas|buenos dias|buenas tardes)\b.*",
                [
                    "¡Hola! Soy ELIZA, tu asistente de películas. ¿Qué te gustaría ver?",
                    "¡Hola! ¿Buscas una película para disfrutar hoy?"
                ]
            ),
            (
                r".*\b(gracias|muchas gracias)\b.*",
                [
                    "¡De nada! Espero que disfrutes la película.",
                    "¡Con gusto! Aquí estaré para recomendarte más películas."
                ]
            ),
            (
                r".*\b(favorita|favorito|me gusta)\b.*",
                [
                    "¡Interesante! ¿Qué es lo que más te gusta de esa película?",
                    "¡Cuéntame más! ¿Qué género disfrutas más?"
                ]
            ),
            (
                r".*",
                [
                    "¡Qué interesante! Cuéntame más sobre tus gustos en el cine.",
                    "No estoy seguro de entender. ¿Cuál es tu película favorita?",
                    "¿Prefieres ver películas en el cine o desde casa?"
                ]
            )
        ]

    def __str__(self):
        return f"{self.nombre} ({len(self.reglas)} reglas)"

    def normalizar(self, texto):
        """Convierte el texto a minúsculas y elimina acentos."""
        texto = texto.lower().strip()
        texto = unicodedata.normalize("NFD", texto)
        texto = "".join(
            caracter for caracter in texto
            if unicodedata.category(caracter) != "Mn"
        )
        return texto

    def responder(self, texto):
        """Busca una regla coincidente y devuelve una respuesta."""
        texto_limpio = self.normalizar(texto)

        if not texto_limpio:
            return "Escribe algo para que pueda recomendarte una película."

        for patron, respuestas in self.reglas:
            if re.search(patron, texto_limpio):
                return random.choice(respuestas)

        return "Cuéntame más sobre tus gustos en el cine."


# Programa principal
if __name__ == "__main__":
    bot = ChatbotPeliculas()

    print(f"--- {bot} inicializado ---")
    print("¡Bienvenido al recomendador de películas!")
    print("Escribe 'salir' para terminar la conversación.\n")

    while True:
        try:
            usuario = input("Tú: ").strip()

            if usuario.lower() == "salir":
                print(f"{bot.nombre}: ¡Hasta pronto! Que disfrutes el cine.")
                break

            respuesta = bot.responder(usuario)
            print(f"{bot.nombre}: {respuesta}\n")

        except (KeyboardInterrupt, EOFError):
            print(f"\n{bot.nombre}: ¡Hasta pronto!")
            break
        