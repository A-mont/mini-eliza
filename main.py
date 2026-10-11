"""Punto de entrada: python main.py"""
from peliculas import ChatbotPeliculas

def main():
    """Ciclo principal de la conversación con el bot de cine."""
    bot = ChatbotPeliculas()
    print(bot)
    historial = []
    
    while True:
        texto = input("Tú: ")
        if texto.lower().strip(" .!¡") in ("adiós", "adios"):
            print(f"{bot.nombre}: ¡Gracias por hablar de cine! ¡Hasta la próxima función!")
            break
            
        respuesta = bot.responder(texto)
        historial.append((texto, respuesta))
        print(f"{bot.nombre}: {respuesta}")
        
    print("\n--- Conversación Completa ---")
    for usuario, bot_dijo in historial:
        print(f"Tú: {usuario}\n{bot.nombre}: {bot_dijo}")

if __name__ == "__main__":
    main()
