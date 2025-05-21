# Definimos una clase Nodo para la lista doblemente enlazada
class Nodo:
    def __init__(self, cancion):
        self.cancion = cancion
        self.siguiente = None
        self.anterior = None

# Definimos una clase ListaReproduccion para manejar la lista de canciones
class ListaReproduccion:
    def __init__(self):
        self.cabeza = None
        self.actual = None
    
    def agregar_cancion(self, cancion):
        nuevo_nodo = Nodo(cancion)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.actual = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = actual
    
    def eliminar_cancion(self, cancion):
        actual = self.cabeza
        while actual:
            if actual.cancion == cancion:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                if self.actual == actual:
                    self.actual = actual.siguiente if actual.siguiente else self.cabeza
                return
            actual = actual.siguiente
    
    def reproducir_siguiente(self):
        if self.actual and self.actual.siguiente:
            self.actual = self.actual.siguiente
            return self.actual.cancion
        return None
    
    def reproducir_anterior(self):
        if self.actual and self.actual.anterior:
            self.actual = self.actual.anterior
            return self.actual.cancion
        return None
    
    def mostrar_lista(self):
        canciones = []
        actual = self.cabeza
        while actual:
            canciones.append(actual.cancion)
            actual = actual.siguiente
        return canciones