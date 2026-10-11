from peliculas import ChatbotPeliculas

def iniciar_chat():
    bot = ChatbotPeliculas()
    print(f"--- {bot} Inicializado ---")
    print("CineBot: ¡Hola! Soy un experto en cine. Dime cómo te llamas o de qué quieres hablar.")
    
    while True:
        entrada_usuario = input("Tú: ")
        
        if entrada_usuario.lower() in ['salir', 'adiós', 'adios', 'chau']:
            nombre = bot.nombre_usuario if bot.nombre_usuario else ""
            print(f"{bot.nombre}: ¡Nos vemos en el próximo estreno {nombre}!")
            break
            
        respuesta = bot.responder(entrada_usuario)
        
        # Interceptamos el marcador de historial para imprimir la lista formateada
        if respuesta == "%historial":
            if bot.historial_peliculas:
                peliculas_formateadas = ", ".join(f"'{p}'" for p in bot.historial_peliculas)
                print(f"{bot.nombre}: Hasta ahora hemos mencionado: {peliculas_formateadas}.")
            else:
                print(f"{bot.nombre}: Todavía no has mencionado ninguna película en nuestra sesión.")
        else:
            print(f"{bot.nombre}: {respuesta}")

if __name__ == "__main__":
    iniciar_chat()
