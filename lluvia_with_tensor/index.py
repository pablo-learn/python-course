"""
Ejemplo súper simple de TensorFlow: ¿Llevo paraguas?
Si llueve mucho (>5) = llevo paraguas (1)
Si llueve poco (<5) = no llevo paraguas (0)
"""

# Importar librerías necesarias
import tensorflow as tf  # TensorFlow: librería principal para machine learning
import numpy as np       # NumPy: manejo de arrays numéricos (requerido por TensorFlow)

# Datos súper simples
# np.array() convierte listas de Python a arrays de NumPy (requerido por TensorFlow)
lluvia = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 100)  # Intensidad de lluvia (0-10)
paraguas = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1] * 100)  # 0=no paraguas, 1=sí paraguas

# Crear modelo súper simple
# tf.keras.Sequential() crea un modelo de capas apiladas (una después de otra)
modelo = tf.keras.Sequential([
    # tf.keras.layers.Dense() crea una capa completamente conectada
    tf.keras.layers.Dense(
        units=1,                    # units: número de neuronas en la capa (1 neurona)
        activation='sigmoid',       # activation: función de activación (sigmoid = 0 a 1)
        input_shape=(1,)            # input_shape: forma de entrada (1 característica)
    )
])

# Compilar modelo
# modelo.compile() configura cómo el modelo va a aprender
modelo.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.01),                    # optimizer: algoritmo de optimización (Adam es inteligente)
    loss='binary_crossentropy',         # loss: función de pérdida para problemas sí/no
    metrics=['accuracy']                # metrics: qué medir durante el entrenamiento (precisión)
)

# Entrenar modelo
print("Entrenando modelo...")
# modelo.fit() entrena el modelo con los datos
modelo.fit(
    lluvia,         # x: datos de entrada (intensidad de lluvia)
    paraguas,       # y: datos de salida (llevar paraguas o no)
    epochs=100,     # epochs: cuántas veces ver todos los datos (100 iteraciones)
    verbose=1       # verbose: mostrar progreso (0=sin mostrar, 1=mostrar)
)

# Probar modelo
print("\nProbando modelo:")
for lluvia_test in [2, 5, 8, 9]:  # Probar con diferentes intensidades de lluvia
    # modelo.predict() hace predicciones con nuevos datos
    prediccion = modelo.predict(
        np.array([lluvia_test]),  # input: array con el valor a predecir
        verbose=0                 # verbose: no mostrar mensajes de TensorFlow
    )
    print(f"prediciendo: {prediccion[0][0]}")
    # La predicción es un valor entre 0 y 1 (probabilidad)
    # Si > 0.5, decimos que lleva paraguas; si < 0.5, no lleva
    resultado = "SÍ" if prediccion[0][0] > 0.5 else "NO"
    print(f"Lluvia {lluvia_test}: {resultado} llevo paraguas")

print("\n¡Listo!")


# NUEVO: Guardar el modelo entrenado
print("\nGuardando modelo...")
modelo.save('modelo_paraguas.keras')
print("Modelo guardado como 'modelo_paraguas.h5'")

print("\n¡Entrenamiento completado y modelo guardado!")