"""Punto de entrada: python main.py"""

from musica import ChatbotMusica

def main():
    """Ciclo principal de la conversación musical."""
    bot = ChatbotMusica()
    print(bot)

    historial = []

    while True:
        texto = input("Tú: ")

        if texto.lower().strip() in ("adiós", "adios", "salir"):
            print(f"{bot.nombre}: ¡Gracias por conversar conmigo! ¡Que nunca te falte la música!")
            break

        respuesta = bot.responder(texto)
        historial.append((texto, respuesta))
        print(f"{bot.nombre}: {respuesta}")

    print("\n--- Historial de la conversación ---")

    for usuario, bot_dijo in historial:
        print(f"Tú: {usuario}\n{bot.nombre}: {bot_dijo}")


if __name__ == "__main__":
    main()