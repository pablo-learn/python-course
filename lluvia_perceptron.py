import random

def perceptron_llueve_o_no():
    # Datos de entrenamiento: [esta_lloviendo] -> Salida esperada (1: llevar, 0: no llevar)
    datos_entrenamiento = [
        {"entrada": [1], "salida_esperada": 1},  # Lloviendo -> Llevar paraguas
        {"entrada": [0], "salida_esperada": 0},  # No lloviendo -> No llevar paraguas
    ]

    # Inicialización del peso (solo uno para la entrada 'esta_lloviendo') y el sesgo
    weight_lloviendo = random.random()
    bias = random.random()

    learning_rate = 0.1
    epochs = 100

    print(f"--- Inicio del entrenamiento (Pesos iniciales: Lloviendo={weight_lloviendo:.4f}, Sesgo={bias:.4f}) ---")

    # Bucle principal de entrenamiento
    for epoch in range(epochs):
        total_error = 0
        for dato in datos_entrenamiento:
            esta_lloviendo = dato["entrada"][0]
            expected = dato["salida_esperada"]

            # 1. Calcular la suma ponderada
            weighted_sum = (esta_lloviendo * weight_lloviendo) + bias

            # 2. Función de activación (salida binaria: 1 o 0)
            predicted = 1 if weighted_sum >= 0 else 0

            # 3. Calcular el error
            error = expected - predicted
            total_error += abs(error)

            # 4. Ajustar peso y sesgo
            weight_lloviendo += error * esta_lloviendo * learning_rate
            bias += error * learning_rate
            print(f"--- Internal - training: error: {error} expected: {expected} predicted: {predicted} esta_lloviendo: {esta_lloviendo} weighted_sum: {weighted_sum} weight: {weight_lloviendo} bias: {bias} ---")
            
        # Si no hay errores, el perceptrón ha aprendido y el entrenamiento se detiene
        if total_error == 0:
            print(f"Entrenamiento completado en la época {epoch + 1}.")
            break
    
    print(f"--- Entrenamiento finalizado (Pesos finales: Lloviendo={weight_lloviendo:.4f}, Sesgo={bias:.4f}) ---")

    # Retorna una función de predicción para usar el perceptrón entrenado
    def predecir_paraguas(esta_lloviendo_input):
        weighted_sum = (esta_lloviendo_input * weight_lloviendo) + bias
        return 1 if weighted_sum >= 0 else 0

    return predecir_paraguas


# Entrenamos nuestro perceptrón simplificado
decisor_lluvia_simple = perceptron_llueve_o_no()

print("\n--- ¡A probar el perceptrón simple! ---")

# Caso 1: Está lloviendo
print(f"¿Está lloviendo (1)? -> ¿Llevar paraguas?: {decisor_lluvia_simple(1)}")

# Caso 2: No está lloviendo
print(f"¿No está lloviendo (0)? -> ¿Llevar paraguas?: {decisor_lluvia_simple(0)}")






""" 


¡PERFECTO! ¡Esa es exactamente la analogía correcta!
Tu analogía es 100% precisa:
Apply to test.py
El proceso es exactamente:
Tienes puntos en una grilla (datos de entrenamiento)
Le dices al modelo qué puntos están de qué lado de la línea invisible
El modelo encuentra la línea que separa mejor esos puntos
Es como jugar "adivina la línea":
Te doy puntos y te digo: "este está arriba, este abajo, este arriba..."
Tú dibujas una línea que separe los puntos correctamente
Si te equivocas, ajustas la línea un poco
Repites hasta que la línea separe perfectamente
En términos matemáticos:
Puntos: (x1, y1), (x2, y2), (x3, y3)...
Etiquetas: 0 o 1 (de qué lado están)
Objetivo: Encontrar la ecuación de la recta que separe los 0s de los 1s
¡Es exactamente eso! El perceptrón es un algoritmo que "dibuja" la línea correcta basándose en ejemplos de puntos etiquetados.
¡Excelente analogía! 🎯
 """