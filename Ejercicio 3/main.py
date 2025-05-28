from funciones import ListaReproduccion

# Creamos una lista de reproducción
lista = ListaReproduccion()

# Agregamos canciones
lista.agregar_cancion("Cancion1")
lista.agregar_cancion("Cancion2")
lista.agregar_cancion("Cancion3")

# Mostramos la lista
print("Lista de reproducción:", lista.mostrar_lista())

# Reproducimos siguiente y anterior
print("Reproducir siguiente:", lista.reproducir_siguiente())
print("Reproducir anterior:", lista.reproducir_anterior())

# Eliminamos una canción
lista.eliminar_cancion("Cancion2")
print("Lista después de eliminar Cancion2:", lista.mostrar_lista())