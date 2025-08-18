# Ejemplos de Anotaciones de Tipo en Python

from typing import List, Dict, Tuple, Optional, Union, Callable, Any
from dataclasses import dataclass

# ============================================================================
# ANOTACIONES BÁSICAS
# ============================================================================

def saludar(nombre: str) -> str:
    """Función básica con anotaciones de tipo."""
    return f"¡Hola {nombre}!"

def suma(a: int, b: int) -> int:
    """Suma de dos enteros."""
    return a + b

def promedio(numeros: List[float]) -> float:
    """Calcula el promedio de una lista de números."""
    return sum(numeros) / len(numeros) if numeros else 0.0

# ============================================================================
# ANOTACIONES CON TIPOS COMPLEJOS
# ============================================================================

def procesar_usuario(
    nombre: str,
    edad: int,
    emails: List[str],
    activo: bool = True
) -> Dict[str, Any]:
    """Procesa datos de usuario con tipos complejos."""
    return {
        "nombre": nombre,
        "edad": edad,
        "emails": emails,
        "activo": activo,
        "timestamp": "2024-01-01"
    }

def obtener_coordenadas() -> Tuple[float, float]:
    """Retorna coordenadas como tupla."""
    return (40.7128, -74.0060)

# ============================================================================
# ANOTACIONES CON OPTIONAL
# ============================================================================

def buscar_usuario(id_usuario: int) -> Optional[Dict[str, Any]]:
    """Busca usuario por ID, puede retornar None."""
    usuarios = {
        1: {"nombre": "Juan", "edad": 30},
        2: {"nombre": "Ana", "edad": 25}
    }
    return usuarios.get(id_usuario)

def dividir(a: float, b: float) -> Optional[float]:
    """División que puede fallar."""
    try:
        return a / b
    except ZeroDivisionError:
        return None

# ============================================================================
# ANOTACIONES CON UNION
# ============================================================================

def procesar_dato(dato: Union[str, int, float]) -> str:
    """Procesa diferentes tipos de datos."""
    return str(dato).upper()

def calcular_area(forma: Union[str, Dict[str, float]]) -> float:
    """Calcula área de diferentes formas."""
    if isinstance(forma, str):
        return 0.0  # Placeholder
    elif isinstance(forma, dict):
        return forma.get("area", 0.0)
    return 0.0

# ============================================================================
# ANOTACIONES CON CALLABLE
# ============================================================================

def aplicar_funcion(
    func: Callable[[int], int],
    valores: List[int]
) -> List[int]:
    """Aplica una función a una lista de valores."""
    return [func(x) for x in valores]

def crear_funcion(multiplicador: int) -> Callable[[int], int]:
    """Crea una función que multiplica por un valor."""
    def multiplicar(x: int) -> int:
        return x * multiplicador
    return multiplicar

# ============================================================================
# ANOTACIONES EN CLASES
# ============================================================================

class Usuario:
    def __init__(self, nombre: str, edad: int, emails: List[str]) -> None:
        self.nombre: str = nombre
        self.edad: int = edad
        self.emails: List[str] = emails
        self.activo: bool = True
    
    def agregar_email(self, email: str) -> None:
        """Agrega un email a la lista."""
        self.emails.append(email)
    
    def obtener_info(self) -> Dict[str, Any]:
        """Retorna información del usuario."""
        return {
            "nombre": self.nombre,
            "edad": self.edad,
            "emails": self.emails,
            "activo": self.activo
        }

# ============================================================================
# ANOTACIONES CON DATACLASS
# ============================================================================

@dataclass
class Producto:
    id: int
    nombre: str
    precio: float
    stock: int
    categorias: List[str]
    
    def esta_disponible(self) -> bool:
        """Verifica si el producto está disponible."""
        return self.stock > 0
    
    def aplicar_descuento(self, porcentaje: float) -> float:
        """Aplica descuento al precio."""
        return self.precio * (1 - porcentaje / 100)

# ============================================================================
# ANOTACIONES CON GENERICS
# ============================================================================

from typing import TypeVar, Generic

T = TypeVar('T')

class Pila(Generic[T]):
    def __init__(self) -> None:
        self.items: List[T] = []
    
    def push(self, item: T) -> None:
        """Agrega un elemento a la pila."""
        self.items.append(item)
    
    def pop(self) -> T:
        """Remueve y retorna el último elemento."""
        return self.items.pop()
    
    def esta_vacia(self) -> bool:
        """Verifica si la pila está vacía."""
        return len(self.items) == 0

# ============================================================================
# ANOTACIONES CON LITERAL
# ============================================================================

from typing import Literal

def procesar_estado(estado: Literal["activo", "inactivo", "pendiente"]) -> str:
    """Procesa estados específicos."""
    return f"Estado: {estado}"

def configurar_modo(modo: Literal["debug", "produccion", "test"]) -> None:
    """Configura el modo de la aplicación."""
    print(f"Modo configurado: {modo}")

# ============================================================================
# ANOTACIONES CON PROTOCOL
# ============================================================================

from typing import Protocol

class Dibujable(Protocol):
    def dibujar(self) -> str:
        ...

class Circulo:
    def __init__(self, radio: float) -> None:
        self.radio = radio
    
    def dibujar(self) -> str:
        return f"Círculo con radio {self.radio}"

def dibujar_forma(forma: Dibujable) -> str:
    """Dibuja cualquier forma que implemente el protocolo."""
    return forma.dibujar()

# ============================================================================
# ANOTACIONES CON NEWTYPE
# ============================================================================

from typing import NewType

UserId = NewType('UserId', int)
Email = NewType('Email', str)

def crear_usuario(user_id: UserId, email: Email) -> Dict[str, Any]:
    """Crea un usuario con tipos personalizados."""
    return {"id": user_id, "email": email}

# ============================================================================
# ANOTACIONES CON ALIASES
# ============================================================================

# Alias para tipos complejos
Configuracion = Dict[str, Union[str, int, bool]]
Resultado = Tuple[bool, str]
ListaUsuarios = List[Usuario]

def cargar_configuracion(ruta: str) -> Configuracion:
    """Carga configuración desde archivo."""
    return {"debug": True, "puerto": 8000, "host": "localhost"}

def procesar_usuarios(usuarios: ListaUsuarios) -> Resultado:
    """Procesa una lista de usuarios."""
    if not usuarios:
        return (False, "No hay usuarios para procesar")
    return (True, f"Procesados {len(usuarios)} usuarios")

# ============================================================================
# ANOTACIONES CON VARIADIC
# ============================================================================

def sumar_todos(*numeros: int) -> int:
    """Suma todos los números proporcionados."""
    return sum(numeros)

def crear_perfil(**datos: str) -> Dict[str, str]:
    """Crea un perfil con datos variables."""
    return datos

# ============================================================================
# EJEMPLOS DE USO
# ============================================================================

def main() -> None:
    """Función principal con ejemplos de uso."""
    
    # Ejemplos básicos
    print(saludar("Python"))
    print(suma(5, 3))
    print(promedio([1.0, 2.0, 3.0, 4.0]))
    
    # Ejemplos con tipos complejos
    usuario = procesar_usuario("Juan", 30, ["juan@email.com"])
    print(usuario)
    
    # Ejemplos con Optional
    resultado = buscar_usuario(1)
    print(resultado)
    
    # Ejemplos con clases
    u = Usuario("Ana", 25, ["ana@email.com"])
    u.agregar_email("ana2@email.com")
    print(u.obtener_info())
    
    # Ejemplos con dataclass
    producto = Producto(1, "Laptop", 999.99, 5, ["Electrónicos", "Computadoras"])
    print(f"Precio con descuento: {producto.aplicar_descuento(10)}")
    
    # Ejemplos con Generic
    pila_numeros = Pila[int]()
    pila_numeros.push(1)
    pila_numeros.push(2)
    print(f"Elemento removido: {pila_numeros.pop()}")
    
    # Ejemplos con Protocol
    circulo = Circulo(5.0)
    print(dibujar_forma(circulo))
    
    # Ejemplos con NewType
    user_id = UserId(123)
    email = Email("usuario@email.com")
    nuevo_usuario = crear_usuario(user_id, email)
    print(nuevo_usuario)
    
    # Ejemplos con Literal
    print(procesar_estado("activo"))
    configurar_modo("debug")
    
    # Ejemplos con variadic
    print(sumar_todos(1, 2, 3, 4, 5))
    perfil = crear_perfil(nombre="Juan", ciudad="Madrid", edad="30")
    print(perfil)

if __name__ == "__main__":
    main()
