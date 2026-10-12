"""Chatbot temático de una pizzería."""
from chatbot import Chatbot


class ChatbotPizzeria(Chatbot):
    """Mesero virtual que toma pedidos de pizza."""

    def __init__(self):
        super().__init__("Pizzero")

        self.reglas = [
            # Saludo
            (r"\b(?:hola|buenos días|buenas tardes|buenas noches)\b",
             ["¡Bienvenido a nuestra pizzería! ¿Qué se te antoja comer?"]),

            # Menú
            (r"\b(?:menú|menu|qué venden|que venden)\b",
             ["Tenemos pizza de pepperoni, hawaiana, mexicana y cuatro quesos. "
              "También ofrecemos refrescos, papas y pan de ajo."]),

            # Pedido de pizza
            (r"\bquiero (.*)",
             ["¡Perfecto! Agregamos {0} a tu pedido. ¿Deseas algo más?",
              "¡Claro! Tu pedido de {0} está anotado. ¿Qué bebida te gustaría?"]),

            # Gustos del cliente
            (r"\bme gusta (.*)",
             ["¡Qué rico! ¿Te gustaría pedir {0} hoy?"]),

            # Algo que no le gusta
            (r"\bno me gusta (.*)",
             ["No hay problema, no agregaremos {0}. ¿Qué otra opción prefieres?"]),

            # Precios
            (r"\b(?:cuánto cuesta|cuanto cuesta|precio|precios)\b.*",
             ["La pizza de pepperoni cuesta $120, la hawaiana $130, "
              "la mexicana $140 y la de cuatro quesos $150."]),

            # Recomendaciones
            (r"\b(?:recomienda|recomiéndame|recomiendame)\b.*",
             ["Te recomiendo la pizza mexicana si te gustan los sabores intensos, "
              "o la de cuatro quesos si prefieres mucho queso."]),

            # Bebidas
            (r"\b(?:bebida|bebidas|refresco|refrescos)\b.*",
             ["Tenemos refrescos de cola, naranja y limón por $25. "
              "¿Cuál te gustaría ordenar?"]),

            # Tamaños
            (r"\b(?:tamaño|tamanos|tamaños)\b.*",
             ["Tenemos pizzas chicas, medianas y grandes. "
              "¿Qué tamaño prefieres?"]),

            # Entregas a domicilio
            (r"\b(?:domicilio|entrega|a domicilio)\b.*",
             ["¡Sí, contamos con servicio a domicilio! "
              "¿En qué zona te encuentras para consultar la cobertura?"]),

            # Tiempo de entrega
            (r"\b(?:cuánto tarda|cuanto tarda|tiempo de entrega)\b.*",
             ["El tiempo de entrega depende de la zona y de la demanda. "
              "Al confirmar tu pedido te indicaremos el tiempo estimado."]),

            # Métodos de pago
            (r"\b(?:pago|pagar|tarjeta|efectivo)\b.*",
             ["Puedes consultar si aceptamos efectivo o tarjeta al confirmar tu pedido. "
              "¿Cómo prefieres pagar?"]),

            # Confirmar pedido
            (r"\b(?:confirmar|confirmo|listo mi pedido)\b.*",
             ["¡Gracias! Tu pedido está listo para confirmarse con el personal."]),

            # Cancelar pedido
            (r"\b(?:cancelar|cancelación|cancelacion)\b.*",
             ["Entiendo que deseas cancelar tu pedido. "
              "Por favor, confirma la cancelación con el personal de la pizzería."]),

            # Agradecimiento
            (r"\b(?:gracias|muchas gracias)\b.*",
             ["¡De nada! Gracias por elegir nuestra pizzería. ¡Esperamos verte pronto!"]),

            # Despedida
            (r"\b(?:adiós|adios|hasta luego|nos vemos)\b",
             ["¡Hasta luego! Gracias por visitarnos. ¡Que tengas un excelente día!"])