import math

def calcular_distancia_total(coordenadas):
    distancia_total = 0
    for i in range(len(coordenadas) - 1):
        x1, y1 = coordenadas[i]
        x2, y2 = coordenadas[i + 1]
        distancia = math.hypot(x2 - x1, y2 - y1)
        distancia_total += distancia
    return distancia_total
# Ejemplo de uso
coordenadas = [(0, 0), (3, 4), (6, 8), (10, 10)]
distancia = calcular_distancia_total(coordenadas)
print(f"La distancia total recorrida es: {distancia}")

