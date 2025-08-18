# Concurrencia y Paralelismo en Python - Guía Completa

## 🔒 **Lock - Explicación Resumida**

### **¿Qué es?**

Un **Lock** es un mecanismo de sincronización que garantiza que **solo un hilo** pueda acceder a un recurso compartido a la vez.

### **¿Para qué sirve?**

-   Evita **race conditions** (condiciones de carrera)
-   Protege datos compartidos entre múltiples hilos
-   Garantiza **consistencia** en operaciones críticas

### **Sintaxis Básica**

```python
import threading

lock = threading.Lock()

def funcion_critica():
    with lock:  # Solo un hilo puede ejecutar este bloque
        # Operaciones con datos compartidos
        pass
```

### **Ejemplo Práctico**

```python
saldo = 0
lock = threading.Lock()

def depositar(cantidad):
    global saldo
    with lock:  # Bloquea acceso
        saldo += cantidad  # Solo un hilo modifica a la vez
```

### **Características Clave**

-   **Exclusivo**: Solo un hilo puede tener el lock
-   **Bloqueante**: Otros hilos esperan hasta que se libere
-   **Context Manager**: Usar `with lock:` es la forma más segura
-   **Simple**: No permite reentrada (un hilo no puede adquirirlo dos veces)

### **Cuándo Usarlo**

-   Variables compartidas entre hilos
-   Operaciones de lectura/escritura en recursos comunes
-   Cualquier operación que deba ser **atómica**

---

## 🔄 **RLock (Reentrant Lock) - Explicación**

### **¿Qué es?**

Un **RLock** es un Lock que permite que el **mismo hilo** lo adquiera **múltiples veces** sin causar un deadlock.

### **¿Por qué se necesita?**

Con un **Lock normal**, si un hilo intenta adquirir el mismo lock dos veces, se bloquea indefinidamente:

```python
# ❌ PROBLEMA con Lock normal
lock = threading.Lock()

def funcion_problema():
    with lock:  # Primera adquisición
        with lock:  # ❌ BLOQUEO - Deadlock!
            print("Nunca se ejecuta")
```

### **✅ SOLUCIÓN con RLock**

```python
rlock = threading.RLock()

def funcion_solucion():
    with rlock:  # Primera adquisición
        with rlock:  # ✅ FUNCIONA - Mismo hilo
            print("Se ejecuta correctamente")
```

### **Casos de Uso Comunes**

**1. Funciones Recursivas:**

```python
class CuentaBancaria:
    def __init__(self):
        self.rlock = threading.RLock()
        self.saldo = 1000

    def transferir(self, cantidad):
        with self.rlock:
            self.saldo -= cantidad
            self.verificar_saldo()  # ✅ Puede usar el mismo lock

    def verificar_saldo(self):
        with self.rlock:  # ✅ Mismo hilo, mismo lock
            if self.saldo < 0:
                print("Saldo insuficiente")
```

**2. Métodos que se Llaman entre Sí:**

```python
def metodo_a():
    with rlock:
        metodo_b()  # ✅ Puede usar el mismo lock

def metodo_b():
    with rlock:  # ✅ Mismo hilo, mismo lock
        print("Operación segura")
```

### **Características Clave**

-   **Reentrante**: El mismo hilo puede adquirirlo múltiples veces
-   **Contador interno**: Lleva la cuenta de cuántas veces lo adquirió el hilo
-   **Liberación gradual**: Se debe liberar tantas veces como se adquirió
-   **Thread-safe**: Solo un hilo puede tener el lock a la vez

### **Cuándo Usar RLock vs Lock**

| Situación                                 | Usar    |
| ----------------------------------------- | ------- |
| **Operaciones simples**                   | `Lock`  |
| **Funciones recursivas**                  | `RLock` |
| **Métodos que se llaman entre sí**        | `RLock` |
| **Lógica compleja con múltiples niveles** | `RLock` |

---

## 🔗 **multiprocessing.Queue y multiprocessing.Value - Resumen**

### **🔗 multiprocessing.Queue**

**¿Qué es?**
Una cola **thread-safe** y **process-safe** para pasar datos entre procesos.

**Características:**

-   **FIFO** (First In, First Out)
-   **Bloqueante** por defecto
-   **Serialización automática** de objetos Python

**Sintaxis básica:**

```python
import multiprocessing

cola = multiprocessing.Queue()

# Enviar datos
cola.put(dato)

# Recibir datos
dato = cola.get()  # Bloquea hasta que haya datos
dato = cola.get_nowait()  # No bloquea (puede fallar)
```

**Ejemplo:**

```python
def worker(cola):
    cola.put("Hola desde proceso hijo")

if __name__ == "__main__":
    cola = multiprocessing.Queue()
    proceso = multiprocessing.Process(target=worker, args=(cola,))
    proceso.start()
    proceso.join()

    mensaje = cola.get()  # "Hola desde proceso hijo"
```

### **🔢 multiprocessing.Value**

**¿Qué es?**
Una variable **compartida** entre procesos para tipos de datos simples (int, float, bool).

**Características:**

-   **Memoria compartida** entre procesos
-   **Tipos específicos** (c, i, f, d, b)
-   **Thread-safe** para operaciones básicas

**Sintaxis básica:**

```python
import multiprocessing

# Crear valor compartido
valor = multiprocessing.Value('i', 0)  # 'i' = int, valor inicial 0

# Acceder al valor
valor.value = 10  # Asignar
print(valor.value)  # Leer
```

**Ejemplo:**

```python
def incrementar(valor_compartido):
    valor_compartido.value += 1

if __name__ == "__main__":
    contador = multiprocessing.Value('i', 0)

    procesos = []
    for _ in range(3):
        p = multiprocessing.Process(target=incrementar, args=(contador,))
        procesos.append(p)
        p.start()

    for p in procesos:
        p.join()

    print(f"Contador final: {contador.value}")  # 3
```

### **📊 Comparación Rápida**

| Característica   | Queue                       | Value                   |
| ---------------- | --------------------------- | ----------------------- |
| **Uso**          | Comunicación entre procesos | Variable compartida     |
| **Datos**        | Cualquier objeto Python     | Solo tipos primitivos   |
| **Operaciones**  | put/get                     | Acceso directo a .value |
| **Complejidad**  | Más complejo                | Más simple              |
| **Casos de uso** | Envío de resultados         | Contadores, flags       |

---

## 🏢 **multiprocessing.Manager - Explicación**

### **¿Qué es?**

Un **Manager** es una herramienta que crea **objetos compartidos** entre procesos, permitiendo que múltiples procesos accedan a las mismas estructuras de datos.

### **¿Por qué se necesita?**

-   Los **procesos no comparten memoria** por defecto
-   **Queue y Value** solo manejan tipos simples
-   **Manager** permite estructuras complejas (listas, diccionarios, etc.)

### **Sintaxis Básica**

```python
import multiprocessing

with multiprocessing.Manager() as manager:
    # Crear objetos compartidos
    lista_compartida = manager.list()
    diccionario_compartido = manager.dict()
    valor_compartido = manager.Value('i', 0)
```

### **Tipos de Objetos Disponibles**

| Tipo            | Creación                | Uso                           |
| --------------- | ----------------------- | ----------------------------- |
| **Lista**       | `manager.list()`        | `lista.append()`, `lista[0]`  |
| **Diccionario** | `manager.dict()`        | `dict['key'] = value`         |
| **Value**       | `manager.Value('i', 0)` | `valor.value = 10`            |
| **Lock**        | `manager.Lock()`        | `with lock:`                  |
| **Event**       | `manager.Event()`       | `event.set()`, `event.wait()` |

### **Ejemplo Práctico**

**Compartir Lista entre Procesos:**

```python
import multiprocessing

def agregar_numeros(lista_compartida, inicio, fin):
    for i in range(inicio, fin):
        lista_compartida.append(i)

if __name__ == "__main__":
    with multiprocessing.Manager() as manager:
        # Crear lista compartida
        numeros_compartidos = manager.list()

        # Crear procesos
        proceso1 = multiprocessing.Process(
            target=agregar_numeros,
            args=(numeros_compartidos, 1, 6)
        )
        proceso2 = multiprocessing.Process(
            target=agregar_numeros,
            args=(numeros_compartidos, 6, 11)
        )

        # Ejecutar procesos
        proceso1.start()
        proceso2.start()
        proceso1.join()
        proceso2.join()

        print(f"Lista final: {list(numeros_compartidos)}")
        # Resultado: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

**Compartir Diccionario:**

```python
def actualizar_estado(dict_compartido, key, value):
    dict_compartido[key] = value

if __name__ == "__main__":
    with multiprocessing.Manager() as manager:
        estado_compartido = manager.dict()

        proceso = multiprocessing.Process(
            target=actualizar_estado,
            args=(estado_compartido, 'status', 'completado')
        )
        proceso.start()
        proceso.join()

        print(f"Estado: {estado_compartido['status']}")  # 'completado'
```

### **Ventajas del Manager**

✅ **Flexibilidad**: Estructuras de datos complejas
✅ **Simplicidad**: API similar a objetos Python normales
✅ **Thread-safe**: Operaciones seguras entre procesos
✅ **Automatización**: Manejo automático de serialización

### **Desventajas**

❌ **Overhead**: Más lento que Queue/Value para datos simples
❌ **Serialización**: Los datos se serializan/deserializan
❌ **Memoria**: Consume más memoria que alternativas nativas

### **Cuándo Usar Manager**

| Situación                             | Alternativa       |
| ------------------------------------- | ----------------- |
| **Listas o diccionarios compartidos** | `Manager`         |
| **Estructuras complejas**             | `Manager`         |
| **Datos simples**                     | `Queue` o `Value` |
| **Comunicación unidireccional**       | `Queue`           |
| **Variables primitivas**              | `Value`           |

---

## 🎯 **Resumen General**

### **Herramientas de Sincronización**

-   **Lock**: Acceso exclusivo simple
-   **RLock**: Acceso reentrante para el mismo hilo
-   **Semaphore**: Control de acceso con límite de hilos

### **Comunicación entre Procesos**

-   **Queue**: Envío de datos entre procesos
-   **Value**: Variables simples compartidas
-   **Manager**: Estructuras complejas compartidas

### **Mejores Prácticas**

1. **Siempre usar** `with lock:` para operaciones críticas
2. **Evitar** compartir estado mutable entre hilos
3. **Usar** `if __name__ == "__main__":` en multiprocessing
4. **Gestionar** correctamente el ciclo de vida de hilos/procesos
5. **Elegir** la herramienta correcta según el caso de uso

### **Casos de Uso Recomendados**

-   **Threading**: I/O bound tasks (web requests, file operations)
-   **Multiprocessing**: CPU bound tasks (cálculos intensivos)
-   **Combinación**: Aplicaciones que requieren ambos tipos de tareas

Con estas herramientas, puedes crear aplicaciones Python robustas, eficientes y escalables que manejen múltiples tareas de forma segura y concurrente.
