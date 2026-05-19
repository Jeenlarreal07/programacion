def analizar_numeros(num1, num2):
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division_entera = num1 // num2
    resultados_finales = (suma, resta, multiplicacion, division_entera)
    return resultados_finales
# Ejemplo de uso
resultado_suma, resultado_resta, resultado_multiplicacion, resultado_division_entera = analizar_numeros(10, 3)
print(f"Suma: {resultado_suma}")
print(f"Resta: {resultado_resta}")
print(f"Multiplicación: {resultado_multiplicacion}")
print(f"División Entera: {resultado_division_entera}")     