import random
import math
def analizar_muestras(n):
    # Generar lista de muestras aleatorias
    muestras = [random.randint(1, 100) for _ in range(n)]
    
    # Eliminar duplicados usando set
    muestras_unicas = set(muestras)
    
    # Calcular la raíz cuadrada del valor máximo
    raiz_max = math.sqrt(max(muestras_unicas))
    
    # Retornar un diccionario con los resultados
    resultado = {
        'muestras': muestras,
        'muestras_unicas': muestras_unicas,
        'raiz_max': raiz_max
    }
    
    return resultado
# Ejemplo de uso
n = 5
resultados = analizar_muestras(n)
print(resultados)   

