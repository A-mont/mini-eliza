#Punto de entrada: python main.py
from videojuegos import ChatbotVideojuegos

def main():
    #Ciclo principal de la conversación.
    bot = ChatbotVideojuegos()
    print(bot)
    historial =[]
    while True:
        texto = input("Tú: ")
        if texto.lower().strip(" .!¡") in ("adiós", "adios"):
            print(f"{bot.nombre}: ¡Gracias por tu visita!")
            break
        respuesta = bot.responder(texto)
        historial.append((texto, respuesta))
        print(f"{bot.nombre}: {respuesta}")
    print("\n--- Conversación ---")
    for usuario, bot_dijo in historial:
        print(f"Tú: {usuario}\n{bot.nombre}: {bot_dijo}")

if __name__ == "__main__":
    main()