from funciones import ListaEnlazada

# Creamos una lista enlazada
lista = ListaEnlazada()

# Agregamos valores
lista.agregar(1)
lista.agregar(2)
lista.agregar(3)

# Buscamos valores
print(lista.buscar(2))  # Valor 2 encontrado en la posición 1
print(lista.buscar(4))  # Valor 4 no está en la lista