class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def is_empty(self):
        return len(self.items) == 0

def reverse_words(sentence):
    # Crear una pila
    stack = Stack()
    # Dividir la frase en palabras
    words = sentence.split()
    # Apilar todas las palabras
    for word in words:
        stack.push(word)
    # Desapilar las palabras para formar la frase invertida
    reversed_sentence = ""
    while not stack.is_empty():
        reversed_sentence += stack.pop() + " "
    # Eliminar el espacio final
    return reversed_sentence.strip()

# Prueba
sentence = "Hola mundo desde UAM"
print(reverse_words(sentence))  # Salida: UAM desde mundo Hola