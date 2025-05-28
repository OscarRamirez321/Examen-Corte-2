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

    def ver_tope(self):
        # Retorna el elemento en el tope sin sacarlo
        if not self.esta_vacia():
            return self.items[-1]
        return None

# Función para obtener la prioridad de un operador
def prioridad_operador(operador):
    if operador == '^':
        return 3
    if operador in ['*', '/']:
        return 2
    if operador in ['+', '-']:
        return 1
    return 0  # Para paréntesis de apertura o cualquier otro caso

# Función para convertir una expresión infija a postfija
def convertir_infija_postfija(expresion):
    pila = Pila()
    expresion_postfija = []

    for simbolo in expresion:
        # Si el símbolo es un operando (letra o número), se agrega directamente a la salida
        if simbolo.isalnum():
            expresion_postfija.append(simbolo)
        # Si es un paréntesis de apertura, se apila
        elif simbolo == '(':
            pila.apilar(simbolo)
        # Si es un paréntesis de cierre, desapilamos hasta encontrar el de apertura
        elif simbolo == ')':
            while not pila.esta_vacia() and pila.ver_tope() != '(':
                expresion_postfija.append(pila.desapilar())
            pila.desapilar()  # Sacamos el '('
        # Si es un operador
        else:
            # Desapilamos operadores con mayor o igual prioridad
            while (not pila.esta_vacia() and pila.ver_tope() != '(' and 
                   prioridad_operador(pila.ver_tope()) >= prioridad_operador(simbolo)):
                expresion_postfija.append(pila.desapilar())
            pila.apilar(simbolo)

    # Vaciamos la pila al final
    while not pila.esta_vacia():
        expresion_postfija.append(pila.desapilar())

    return ''.join(expresion_postfija)

# Función para evaluar una expresión postfija
def evaluar_postfija(expresion):
    pila = Pila()

    for simbolo in expresion:
        # Si el símbolo es un operando (número), lo apilamos
        if simbolo.isdigit():
            pila.apilar(int(simbolo))
        # Si es un operador, desapilamos dos operandos y realizamos la operación
        else:
            operando2 = pila.desapilar()
            operando1 = pila.desapilar()
            if simbolo == '+':
                pila.apilar(operando1 + operando2)
            elif simbolo == '-':
                pila.apilar(operando1 - operando2)
            elif simbolo == '*':
                pila.apilar(operando1 * operando2)
            elif simbolo == '/':
                pila.apilar(operando1 / operando2)
            elif simbolo == '^':
                pila.apilar(operando1 ** operando2)

    # El resultado final estará en el tope de la pila
    return pila.desapilar()