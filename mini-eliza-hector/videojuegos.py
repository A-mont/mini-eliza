#Chatbot temático para hablar de videojuegos
from chatbot import Chatbot

class ChatbotVideojuegos(Chatbot):
    def __init__(self, nombre="Videojuegos"):
        super().__init__(nombre)
        self.reglas = [
            (r"\b(?:hola|buenos días|buenas tardes|buenas noches)\b", [
    "¡Hola! ¿De qué videojuego quieres hablar?",
    "¡Hola! ¿Qué has estado jugando últimamente?"
]),
            (r"me gusta jugar a (.*)", ["¡A mí también me gusta jugar a {}!", "¡Qué divertido! ¿Cuánto tiempo llevas jugando a {}?"]),
            (r"no me gusta (.*)", ["¿Por qué no te gusta {}?", "¡Vaya! A mí sí me gusta {}."]),
            (r"mi juego favorito es (.*)", ["¡Genial! Yo también disfruto de {}.", "¡Interesante! ¿Qué te gusta de {}?"]),
            (r"prefiero (.*) a (.*)", ["¿Por qué prefieres {} a {}?", "¡Eso es interesante! ¿Qué te hace preferir {} sobre {}?"]),
            (r"juego en línea", ["¡Los juegos en línea son muy populares! ¿Cuál es tu favorito?", "¡Sí! Los juegos en línea pueden ser muy divertidos."]),
            (r"juego de consola", ["¡Los juegos de consola tienen su encanto! ¿Cuál es tu consola favorita?", "¡Sí! Los juegos de consola ofrecen una gran experiencia."]),
            (r"juego de PC", ["¡Los juegos de PC son geniales! ¿Cuál es tu juego favorito para PC?", "¡Sí! Los juegos de PC ofrecen muchas opciones y personalización."]),
        ]