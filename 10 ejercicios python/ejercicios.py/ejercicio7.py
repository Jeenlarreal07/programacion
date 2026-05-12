'''Tabulador Multiplicador Dinámico ✖️
Enunciado: Imprime la tabla de un número, pero sáltate los resultados que sean impares.
Requerimientos: Función con base y límite. Usa for con range(), y un if con módulo (%) para filtrar.'''
def tabulador_multiplicador(base, limite):
    for i in range(1, limite + 1):
        resultado = base * i
        if resultado % 2 == 0:
            print(f"{base} x {i} = {resultado}")    
# Ejemplo de uso
numero = 5 # Número base para la tabla  
limite = 10 # Límite de la tabla
print(f"Tabla de multiplicar del {numero} (solo resultados pares):")    
tabulador_multiplicador(numero, limite) 

