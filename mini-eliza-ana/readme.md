"""punto de entrada:python main.py""""

from pizza import Chatbotpizza

def main():

"""Ciclo principal de la conversación.""""

bot Chatbotpizza()

print(bot)

historial = []

while True:

texto input("Tú: ")

if texto.lower().strip("1") in ("adiós", "adios"): print(f"(bot.nombre): ¡Gracias por tu visita!")

break

respuesta bot.responder (texto)

historial.append((texto, respuesta))

print(f"(bot.nombre): (respuesta)")

print("\n--- Conversación.")

for usuario, bot_dijo in historial:

print("Tú: (usuario)\n(bot.nombre): (bot_dijo)")

if _name_="main__":
main()