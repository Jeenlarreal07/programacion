"""Sumatoria Condicionada de Pares 🔢
Enunciado: Suma todos los números pares desde el 1 hasta un límite que tú elijas.
Requerimientos: Función con un límite. Usa bucle, condicional con operador módulo (%) para hallar pares y suma al acumulador."""
def sumatoria_pares(limite):
    suma = 0
    for numero in range(1, limite + 1):
        if numero % 2 == 0:
            suma += numero
    return suma
# Ejemplo de uso
limite = 20 # Límite hasta donde sumar los pares
resultado = sumatoria_pares(limite) 
print(f"La sumatoria de los números pares desde 1 hasta {limite} es: {resultado}")  
