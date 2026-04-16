import string
import random

# -----------------------------
# BASE DE CONOCIMIENTO
# -----------------------------
knowledge_base = {
    "señales": [
        {
            "patterns": [
                "qué significa la señal de alto",
                "para qué sirve el pare",
                "qué hago cuando veo stop",
                "qué significa detenerse"
            ],
            "answer": "La señal de ALTO (PARE) significa que debés detener completamente tu vehículo antes de la línea de parada."
        },
        {
            "patterns": [
                "qué es ceda el paso",
                "qué significa ceder",
                "cómo funciona ceda el paso",
                "cuando veo un ceda qué hago"
            ],
            "answer": "La señal de CEDA EL PASO indica que debés reducir la velocidad y dejar pasar a los vehículos con prioridad."
        }
    ],
    "prioridad": [
        {
            "patterns": [
                "quién pasa primero en una rotonda",
                "cómo funciona la rotonda"
            ],
            "answer": "En una rotonda, los vehículos dentro tienen prioridad. Debés ceder el paso antes de entrar."
        }
    ]
}

# -----------------------------
# MEMES POR CATEGORÍA
# -----------------------------
memes = {
    "señales": [
        "six seven 😎",
        "STOP means STOP bro 🛑",
        "no te la juegues 💀",
        "esto es clave para el examen 👁️",
        "cuando lo ignoras... 💀"
    ],
    "prioridad": [
        "el que está adentro gana easy 🗿",
        "turno basado en lógica 🧠",
        "please speed i need this 🏃",
        "AY AY AYYY AY 🗣️",
        "esto cae fijo en el examen 💀"
    ],
    "default": [
        "cuando estudias para el examen en python 💀",
        "mi lente de contacto 👁️",
        "six seven 😎",
        "xd",
        "esto es cine 🚬"
    ]
}

# -----------------------------
# LIMPIEZA DE TEXTO
# -----------------------------
def limpiar_texto(texto):
    texto = texto.lower()

    for signo in string.punctuation:
        texto = texto.replace(signo, "")

    tokens = texto.split()

    stopwords = ["el", "la", "de", "que", "a", "en", "y", "es"]

    tokens_limpios = []

    for palabra in tokens:
        if palabra not in stopwords:
            tokens_limpios.append(palabra)

    return tokens_limpios

# -----------------------------
# DETECTAR INTENCIÓN
# -----------------------------
def detectar_intencion(tokens):
    if "hola" in tokens:
        return "saludo"
    if "gracias" in tokens:
        return "despedida"
    return "pregunta"

# -----------------------------
# COINCIDENCIA
# -----------------------------
def calcular_coincidencia(tokens_usuario, pattern):
    coincidencias = 0
    pattern_tokens = pattern.lower().split()

    for token in tokens_usuario:
        if token in pattern_tokens:
            coincidencias += 1

    return coincidencias

# -----------------------------
# BUSCAR RESPUESTA
# -----------------------------
def buscar_respuesta(tokens_usuario):
    mejor_respuesta = None
    mejor_categoria = "default"
    max_coincidencias = 0

    for categoria in knowledge_base:
        for item in knowledge_base[categoria]:
            for pattern in item["patterns"]:
                score = calcular_coincidencia(tokens_usuario, pattern)

                if score > max_coincidencias:
                    max_coincidencias = score
                    mejor_respuesta = item["answer"]
                    mejor_categoria = categoria

    return mejor_respuesta, mejor_categoria

# -----------------------------
# PERSONALIDAD
# -----------------------------
def agregar_personalidad(respuesta, categoria):
    meme_lista = memes.get(categoria, memes["default"])
    meme1 = random.choice(meme_lista)
    meme2 = random.choice(meme_lista)
    return f"{respuesta} — {meme1} | {meme2}"

# -----------------------------
# GENERAR RESPUESTA
# -----------------------------
def generar_respuesta(intencion, respuesta_base, categoria):
    if intencion == "saludo":
        return "Qué onda amigazo 😎 soy Ruedi, listo para salvar ese examen 🚗"

    if intencion == "despedida":
        return "De una amigazo, éxito total 🚗🔥"

    if intencion == "pregunta":
        if respuesta_base:
            return agregar_personalidad(respuesta_base, categoria)
        else:
            return agregar_personalidad("No encontré info de eso, pero seguimos en modo estudio", "default")

    return "No logré entender eso bien, probá con otra pregunta 🚗"

# -----------------------------
# CHATBOT
# -----------------------------
def chatbot():
    print("Ruedi 🤖 modo chaviza activado. Escribí 'salir' para terminar.\n")

    while True:
        user_input = input("Vos: ")

        if user_input.lower() == "salir":
            break

        tokens = limpiar_texto(user_input)
        intencion = detectar_intencion(tokens)
        respuesta_base, categoria = buscar_respuesta(tokens)
        respuesta_final = generar_respuesta(intencion, respuesta_base, categoria)

        print("Ruedi:", respuesta_final)

# -----------------------------
# EJECUTAR
# -----------------------------
chatbot()
