''''Validador de Secuencias Numéricas 📏
Enunciado: Crea secuencias (inicio, fin, paso). Si el paso es negativo, verifica lógicamente que inicio > fin.
Requerimientos: Función con 3 parámetros. Usa operadores de comparación en un if inicial, luego un while para generar la lista de números. Retorna la lista generada.'''
def validador_secuencias(inicio, fin, paso):
    if paso == 0:
        raise ValueError("El paso no puede ser cero.")
    if (paso > 0 and inicio > fin) or (paso < 0 and inicio < fin):
        raise ValueError("La secuencia no es lógica con el paso dado.")
    
    secuencia = []
    while (paso > 0 and inicio <= fin) or (paso < 0 and inicio >= fin):
        secuencia.append(inicio)
        inicio += paso
    return secuencia
# Ejemplo de uso
inicio = 10 # Número de inicio de la secuencia  
fin = 0 # Número de fin de la secuencia
paso = -2 # Paso de la secuencia (negativo para contar hacia atrás)     
try:
    resultado = validador_secuencias(inicio, fin, paso)
    print(f"Secuencia generada: {resultado}")   
except ValueError as e:
    print(f"Error: {e}")    
    