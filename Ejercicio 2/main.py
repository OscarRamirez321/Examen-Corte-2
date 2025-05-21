from funciones import verificar_parentesis

# Solicitamos al usuario que ingrese una cadena con paréntesis
cadena = input("Ingrese una cadena con paréntesis para verificar: ")

# Verificamos si los paréntesis están balanceados
resultado = verificar_parentesis(cadena)

# Mostramos el resultado
print("¿Paréntesis balanceados?:", resultado)