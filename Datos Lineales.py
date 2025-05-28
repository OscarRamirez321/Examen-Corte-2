# Modulo para la estructura de datos Cola
class Cola:
    def __init__(self):
        """Inicializa una nueva cola vacía."""
        self.items = []

    def esta_vacia(self):
        """Verifica si la cola está vacía."""
        return len(self.items) == 0

    def encolar(self, item):
        """Agrega un elemento al final de la cola."""
        self.items.append(item)

    def desencolar(self):
        """Remueve y retorna el elemento del frente de la cola.
        
        Levanta un IndexError si la cola está vacía.
        """
        if self.esta_vacia():
            raise IndexError("Desencolar de una cola vacía")
        return self.items.pop(0)

    def tamano(self):
        """Retorna el número de elementos en la cola."""
        return len(self.items)

    def __str__(self):
        """Representación en cadena de la cola."""
        return f"Cola: {self.items}"

# Modulo para la estructura de datos Pila
class Pila:
    def __init__(self):
        """Inicializa una nueva pila vacía."""
        self.items = []

    def esta_vacia(self):
        """Verifica si la pila está vacía."""
        return len(self.items) == 0

    def apilar(self, item):
        """Agrega un elemento a la parte superior de la pila."""
        self.items.append(item)

    def desapilar(self):
        """Remueve y retorna el elemento de la parte superior de la pila.
        
        Levanta un IndexError si la pila está vacía.
        """
        if self.esta_vacia():
            raise IndexError("Desapilar de una pila vacía")
        return self.items.pop()

    def tamano(self):
        """Retorna el número de elementos en la pila."""
        return len(self.items)

    def __str__(self):
        """Representación en cadena de la pila."""
        # La pila se mostrará con el último elemento agregado a la derecha (cima)
        return f"Pila: {self.items}"

# Modulo principal con la lógica de separación
def separar_elementos(cola_original):
    """
    Procesa una cola, manteniendo elementos en posiciones pares en la cola
    y transfiriendo elementos en posiciones impares a una pila.

    Args:
        cola_original (Cola): La cola inicial con los elementos.

    Returns:
        tuple: Una tupla que contiene la cola resultante (solo con pares)
               y la pila resultante (con impares).
    """
    cola_resultante = Cola()
    pila_impares = Pila()
    
    posicion = 0
    # Se recorre la cola una sola vez [cite: 4]
    while not cola_original.esta_vacia():
        elemento = cola_original.desencolar()
        
        # La posición de los elementos se cuenta a partir de cero [cite: 3]
        if posicion % 2 == 0:  # Posición par (0, 2, 4, ...)
            cola_resultante.encolar(elemento) # Permanecen en la cola [cite: 1]
        else:  # Posición impar (1, 3, 5, ...)
            pila_impares.apilar(elemento) # Se transfieren a la pila [cite: 2]
        
        posicion += 1
        
    return cola_resultante, pila_impares

# Ejemplo de uso
if __name__ == "__main__":
    # Cola original de ejemplo [cite: 6]
    cola_ejemplo = Cola()
    cola_ejemplo.encolar('A')
    cola_ejemplo.encolar('B')
    cola_ejemplo.encolar('C')
    cola_ejemplo.encolar('D')
    cola_ejemplo.encolar('E')

    print(f"Cola original: {cola_ejemplo.items}")

    # Realizar la separación
    cola_final, pila_final = separar_elementos(cola_ejemplo)

    # Mostrar resultados [cite: 6]
    print(f"Cola resultante: {cola_final.items}")
    print(f"Pila resultante: {pila_final.items}") # La pila contiene los elementos impares en orden LIFO [cite: 5]

    # Otro ejemplo
    print("\n--- Segundo ejemplo ---")
    cola_ejemplo2 = Cola()
    cola_ejemplo2.encolar(10)
    cola_ejemplo2.encolar(20)
    cola_ejemplo2.encolar(30)
    cola_ejemplo2.encolar(40)
    cola_ejemplo2.encolar(50)
    cola_ejemplo2.encolar(60)

    print(f"Cola original: {cola_ejemplo2.items}")
    cola_final2, pila_final2 = separar_elementos(cola_ejemplo2)
    print(f"Cola resultante: {cola_final2.items}")
    print(f"Pila resultante: {pila_final2.items}")