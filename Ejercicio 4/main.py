from funciones import ColaPrioridad

# Creamos una cola de prioridad
cola = ColaPrioridad()

# Agregamos elementos con prioridades
cola.encolar("Tarea1", 3)
cola.encolar("Tarea2", 1)
cola.encolar("Tarea3", 2)

# Desencolamos y mostramos los elementos
print("Desencolar:", cola.desencolar())  # Tarea2 (prioridad 1)
print("Desencolar:", cola.desencolar())  # Tarea3 (prioridad 2)
print("Desencolar:", cola.desencolar())  # Tarea1 (prioridad 3)