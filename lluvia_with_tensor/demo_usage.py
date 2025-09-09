"""
Demo: Usar el modelo ya entrenado para predicciones
"""

import tensorflow as tf
import numpy as np

def cargar_modelo():
    """Carga el modelo previamente entrenado"""
    try:
        print("Cargando modelo entrenado...")
        modelo = tf.keras.models.load_model('modelo_paraguas.keras')
        print("✅ Modelo cargado exitosamente!")
        return modelo
    except FileNotFoundError:
        print("❌ Error: No se encontró el archivo 'modelo_paraguas.keras'")
        print("Primero ejecuta 'python index.py' para entrenar y guardar el modelo")
        return None

def predecir_paraguas(modelo, intensidad_lluvia):
    """Predice si llevar paraguas según la intensidad de lluvia"""
    # Hacer predicción
    prediccion = modelo.predict(
        np.array([intensidad_lluvia]), 
        verbose=0  # Sin mensajes de TensorFlow
    )
    
    # Convertir probabilidad a decisión
    probabilidad = prediccion[0][0]
    decision = "SÍ" if probabilidad > 0.5 else "NO"
    
    return decision, probabilidad

def main():
    # Cargar modelo
    modelo = cargar_modelo()
    if modelo is None:
        return
    
    print("\n🌧️  Demo: ¿Llevo paraguas?")
    print("=" * 30)
    
    # Probar con diferentes valores
    valores_test = [1, 3, 5, 7, 9, 10]
    
    for lluvia in valores_test:
        decision, probabilidad = predecir_paraguas(modelo, lluvia)
        print(f"Lluvia {lluvia}/10: {decision} llevo paraguas (probabilidad: {probabilidad:.2f})")
    
    # Modo interactivo
    print("\n" + "=" * 30)
    print("Prueba tus propios valores:")
    
    while True:
        try:
            entrada = input("\nIntensidad de lluvia (0-10, o 'salir'): ")
            if entrada.lower() in ['salir', 'exit', 'quit']:
                break
            
            intensidad = float(entrada)
            if 0 <= intensidad <= 10:
                decision, probabilidad = predecir_paraguas(modelo, intensidad)
                print(f"🌂 Resultado: {decision} llevo paraguas (confianza: {probabilidad:.2f})")
            else:
                print("⚠️  Por favor ingresa un valor entre 0 y 10")
                
        except ValueError:
            print("⚠️  Por favor ingresa un número válido")
        except KeyboardInterrupt:
            break
    
    print("\n👋 ¡Hasta luego!")

if __name__ == "__main__":
    main()