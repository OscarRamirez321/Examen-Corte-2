# Definimos una clase Pila para implementar la estructura tipo LIFO
class Pila:
    def __init__(self):
        # Lista interna para almacenar los elementos de la pila
        self.items = []

    def esta_vacia(self):
        # Verifica si la pila está vacía
        return len(self.items) == 0

    def apilar(self, item):
        # Agrega un elemento al tope de la pila
        self.items.append(item)

    def desapilar(self):
        # Elimina y retorna el elemento en el tope de la pila
        if not self.esta_vacia():
            return self.items.pop()
        return None

# Función que verifica si los paréntesis en una cadena están balanceados
def verificar_parentesis(cadena):
    pila = Pila()  # Creamos una pila vacía
    pares = {')': '(', '}': '{', ']': '['}  # Diccionario de pares de paréntesis

    for caracter in cadena:
        if caracter in '({[':  # Si es un paréntesis de apertura, lo apilamos
            pila.apilar(caracter)
        elif caracter in ')}]':  # Si es un paréntesis de cierre
            if pila.esta_vacia():  # No hay apertura correspondiente
                return False
            ultimo_apertura = pila.desapilar()
            if ultimo_apertura != pares[caracter]:  # Verificamos si coincide
                return False
    
    # La pila debe estar vacía para que los paréntesis estén balanceados
    return pila.esta_vacia()