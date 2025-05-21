from funciones import convertir_infija_postfija, evaluar_postfija

# Solicitamos al usuario que ingrese una expresión infija
expresion = input("Ingrese una expresión infija (use espacios entre símbolos): ")

# Convertimos la expresión infija a postfija
expresion_postfija = convertir_infija_postfija(expresion.split())
print("Expresión postfija:", expresion_postfija)

# Evaluamos la expresión postfija (solo si contiene números y operadores)
try:
    resultado = evaluar_postfija(expresion_postfija)
    print("Resultado de la evaluación:", resultado)
except:
    print("La expresión contiene variables o no es válida para evaluación numérica.")