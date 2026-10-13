"""Punto de entrada del chatbot de películas."""

from peliculas import ChatbotPeliculas


def main():
    """Ejecuta el ciclo principal de conversación."""
    bot = ChatbotPeliculas()

    print("===================================")
    print("       CHATBOT DE PELÍCULAS")
    print("===================================")
    print(bot)
    print("Escribe 'adiós' para terminar.\n")

    historial = []

    while True:
        texto = input("Tú: ")

        if texto.lower().strip(" .!¡¿") in ("adiós", "adios"):
            print(f"{bot.nombre}: ¡Gracias por hablar de películas!")
            break

        respuesta = bot.responder(texto)
        historial.append((texto, respuesta))

        print(f"{bot.nombre}: {respuesta}")

    print("\n--- Conversación ---")

    for usuario, bot_dijo in historial:
        print(f"Tú: {usuario}")
        print(f"{bot.nombre}: {bot_dijo}")


if __name__ == "__main__":
    main()