# Definimos una clase ColaPrioridad para manejar elementos con prioridades
class ColaPrioridad:
    def __init__(self):
        # Lista interna para almacenar elementos con sus prioridades
        self.items = []

    def esta_vacia(self):
        # Verifica si la cola está vacía
        return len(self.items) == 0

    def encolar(self, elemento, prioridad):
        # Agrega un elemento con su prioridad y ordena la lista
        self.items.append((elemento, prioridad))
        self.items.sort(key=lambda x: x[1])  # Ordenar por prioridad

    def desencolar(self):
        # Elimina y retorna el elemento con menor prioridad
        if not self.esta_vacia():
            return self.items.pop(0)[0]
        return None