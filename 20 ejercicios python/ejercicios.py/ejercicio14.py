def factorial_iterativo(n):
    if n < 0:
        return "Error: El número no puede ser negativo."
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        while n > 1:
            resultado *= n
            n -= 1
        return resultado
# Ejemplo de uso
numero = 5
print(f"El factorial de {numero} es: {factorial_iterativo(numero)}")

