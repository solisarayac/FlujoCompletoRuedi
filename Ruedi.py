import string

# -----------------------------
# BASE DE CONOCIMIENTO COMPLETA
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
            "answer": "La señal de ALTO (PARE) significa que debés detener completamente tu vehículo antes de la línea de parada. No podés avanzar hasta asegurarte de que no hay peligro. ¡Nunca pasés de largo!"
        },
        {
            "patterns": [
                "qué es ceda el paso",
                "qué significa ceder",
                "cómo funciona ceda el paso",
                "cuando veo un ceda qué hago"
            ],
            "answer": "La señal de CEDA EL PASO indica que debés reducir la velocidad y dejar pasar a los vehículos que tienen prioridad."
        },
        {
            "patterns": [
                "qué significa la señal de no pasar",
                "cuándo no puedo adelantar",
                "qué indica línea amarilla continua",
                "puedo adelantar con línea amarilla"
            ],
            "answer": "La línea amarilla continua prohíbe el adelantamiento. Debés mantenerte en tu carril."
        }
    ],

    "prioridad": [
        {
            "patterns": [
                "quién pasa primero en una rotonda",
                "cómo funciona la rotonda",
                "tengo prioridad en el redondel",
                "a quién le cedo en la rotonda"
            ],
            "answer": "En una rotonda, los vehículos dentro tienen prioridad. Debés ceder el paso antes de entrar."
        },
        {
            "patterns": [
                "qué pasa en un cruce sin señales",
                "quién tiene la vía en intersección",
                "a quién le doy el paso en cruce sin semáforo",
                "regla de la derecha en cruce"
            ],
            "answer": "En un cruce sin señales, cedés el paso al vehículo de la derecha."
        }
    ],

    "normas_circulacion": [
        {
            "patterns": [
                "puedo usar el teléfono manejando",
                "es ilegal usar el celular manejando"
            ],
            "answer": "Está prohibido usar el celular mientras manejás, salvo manos libres."
        }
    ],

    "limites_velocidad": [
        {
            "patterns": [
                "límite de velocidad en ciudad",
                "velocidad máxima en zona urbana"
            ],
            "answer": "En ciudad el límite general es 40 km/h."
        }
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

    stopwords = [
        "el", "la", "los", "las", "de", "del", "que",
        "como", "cuando", "a", "en", "un", "una", "y",
        "es", "qué", "para"
    ]

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
    max_coincidencias = 0

    for categoria in knowledge_base:
        for item in knowledge_base[categoria]:
            for pattern in item["patterns"]:

                score = calcular_coincidencia(tokens_usuario, pattern)

                if score > max_coincidencias:
                    max_coincidencias = score
                    mejor_respuesta = item["answer"]

    return mejor_respuesta

# -----------------------------
# GENERAR RESPUESTA FINAL
# -----------------------------
def generar_respuesta(intencion, respuesta_base):
    if intencion == "saludo":
        return "Hola 🚗 soy Ruedi, ¿en qué te ayudo?"

    if intencion == "despedida":
        return "¡Pura vida! 🚗"

    if intencion == "pregunta":
        if respuesta_base:
            return respuesta_base
        else:
            return "No encontré información sobre eso 😅"

    return "No entendí tu mensaje"

# -----------------------------
# CHATBOT
# -----------------------------
def chatbot():
    print("Ruedi 🤖 listo para ayudarte. Escribí 'salir' para terminar.\n")

    while True:
        user_input = input("Vos: ")

        if user_input.lower() == "salir":
            break

        tokens = limpiar_texto(user_input)
        intencion = detectar_intencion(tokens)
        respuesta_base = buscar_respuesta(tokens)
        respuesta_final = generar_respuesta(intencion, respuesta_base)

        print("Ruedi:", respuesta_final)


chatbot()