def main():
    from peliculas import ChatbotPeliculas

    """Ciclo principal de la conversación automática."""
    bot = ChatbotPeliculas()  # Revisa que coincida con el nombre de tu clase
    print(bot)
    
    # 1. Definimos la lista de frases automáticas para la prueba
    frases_prueba = [
        "Hola buenas noches",
        "Quiero ver una película de terror",
        "Me gusta el suspenso",
        "No me gusta el romance",
        "¿Cuál es tu película favorita?",
        "adiós"
    ]
    
    historial = []
    
    # 2. El ciclo recorre la lista de forma automática
    for texto in frases_prueba:
        print(f"Tú: {texto}")  # Muestra lo que simula decir el usuario
        
        if texto.lower().strip(" .!¡") in ("adiós", "adios"):
            print(f"{bot.nombre}: ¡Gracias por tu visita!")
            break
            
        respuesta = bot.responder(texto)
        historial.append((texto, respuesta))
        print(f"{bot.nombre}: {respuesta}")
        print("-" * 20)  # Separador visual entre turnos
        
    print("\n--- Conversación Final ---")
    for usuario, bot_dijo in historial:
        print(f"Tú: {usuario}\n{bot.nombre}: {bot_dijo}")

if __name__ == "__main__":
    main()
