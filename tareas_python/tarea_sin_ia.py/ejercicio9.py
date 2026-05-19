import random
import math
punto1 = (random.randint(0, 10), random.randint(0, 10))
punto2 = (random.randint(0, 10), random.randint(0, 10))
def calcular_distancia(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    resta_x = x2 - x1
    resta_y = y2 - y1
    distancia = math.sqrt((resta_x ** 2) + (resta_y ** 2))
    return distancia
punto1 = (random.randint(0, 10), random.randint(0, 10))
punto2 = (random.randint(0, 10), random.randint(0, 10))
distancia_final = calcular_distancia(punto1, punto2)
print(f"punto 1: {punto1}")
print(f"punto 2: {punto2}")
print(f"la distancia entre los puntos es: {round(distancia_final, 2)}")