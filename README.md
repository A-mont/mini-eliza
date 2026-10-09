# 🤖 Proyecto · Mini-ELIZA (60 %)

**Asignatura:** Inteligencia Artificial · Séptimo semestre
**Modalidad:** Individual
**Valor:** 60 % 

---

## 🎯 Objetivo

Construir en Python, usando clases (POO), un chatbot al estilo **ELIZA** sobre un tema que tú elijas.

ELIZA (Joseph Weizenbaum, MIT, 1966) fue uno de los primeros chatbots: reconocía patrones en lo que escribía el usuario y respondía con frases predefinidas, reflejando sus palabras («yo» → «tú», «mi» → «tu»). No entendía nada, pero muchas personas sentían que sí.

---

## 📋 Instrucciones

- Entrega por **pull request** en el repositorio del curso, en una rama `proyecto/eliza-<tu-apellido>`.
- Haz al menos **3 commits** con mensajes claros.
- Incluye un `README.md` breve con:
  - qué hace tu bot,
  - cómo correrlo,
  - una captura de la salida.
- El programa debe correr sin errores con:

```bash
python main.py
```

- Entrega además un **documento en PDF** con la descripción de tu proyecto y el **enlace público a tu repositorio**.

---

## ⚙️ Requisitos del programa

1. Clase `Chatbot` con los atributos `reflejos` (dict) y `reglas` (lista de patrón y respuestas), y los métodos `reflejar()` y `responder(texto)`.
2. Una subclase de tu tema, por ejemplo `ChatbotCafeteria(Chatbot)`, que llame a `super().__init__()` y agregue al menos **5 reglas con regex**, más un comodín al final.
3. Al menos **2 reglas** que usen `{0}` para devolver, ya reflejado, lo que escribió el usuario.
4. Ciclo principal `while True` que termina cuando el usuario escribe «adiós».
5. Método `__str__` que muestre el nombre del bot y cuántas reglas tiene.

> **Reto opcional:** guarda la conversación en una lista y muéstrala al despedirse.

---

## 💡 Temas sugeridos

Elige uno o propón otro:

| Tema | Usuario escribe… | El bot responde |
|---|---|---|
| **Cafetería** | `quiero (.*)` | `¿Con qué acompañas tu {0}?` |
| **Orientador escolar** | `no entiendo (.*)` | `¿Qué parte de {0} se te complica?` |
| **Videojuegos** | `me gusta (.*)` | `¿Qué es lo que más disfrutas de {0}?` |
| **Mascotas** | `mi perro (.*)` | `¿Desde cuándo tu perro {0}?` |

---

## 💭 Reflexión (en tu README)

Incluye una **conversación de ejemplo de 6 turnos** y responde en **3 líneas**: ¿tu bot «comprende» lo que le escriben? Relaciónalo con el **efecto ELIZA**.

---

## 📊 Rúbrica (60 puntos)

| Criterio | Puntos |
|---|:---:|
| **Funciona:** corre sin errores y cumple los 5 requisitos | 20 |
| **POO:** clase base, herencia o métodos bien usados, `self` y constructor | 15 |
| **Git y GitHub:** rama, 3+ commits claros y PR con descripción | 10 |
| **Explicación:** README con conversación de ejemplo y reflexión | 10 |
| **Buenas prácticas:** PEP 8, nombres claros y docstrings | 5 |
| **Total** | **60** |

---

## 🔗 Recursos

- [Módulo `re` (expresiones regulares) – Documentación de Python](https://docs.python.org/es/3/library/re.html)
- [Clases en Python – Tutorial oficial](https://docs.python.org/es/3/tutorial/classes.html)
- [PEP 8 – Guía de estilo para Python](https://peps.python.org/pep-0008/)