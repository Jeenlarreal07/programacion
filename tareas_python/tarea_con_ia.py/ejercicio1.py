import random
import math
def analizar_muestras(n):
    lista_muestras = []
    for i in range(n):
        numero_al_alzar = random.randint(1, 50)
        lista_muestras.append(numero_al_alzar)
               
        conjunto_limpio = set(lista_muestras)
        valor_maximo = max(conjunto_limpio)
        raiz_maximo = math.sqrt(valor_maximo)
        reporte = {
            "lista_original":lista_muestras,
            "lista_sin_repetidos":conjunto_limpio,
            "lista_maxima":round(raiz_maximo, 2)
        }
    return reporte
resultado_final = analizar_muestras(10)
print("==REPORTE DE MUESTRA==\n")
print(f"lista original:{resultado_final['lista_original']}")
print(f"lista sin repetidos:{resultado_final['lista_sin_repetidos']}")
print(f"raíz cuadrada del valor máximo:{resultado_final['lista_maxima']}")
