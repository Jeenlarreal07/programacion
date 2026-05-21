import random
import math
print("===PROCEDOR DE PRECIOS AUTOMÁTICO===\n")
productos_tupla = ("manzana", "banana", "naranja", "pera", "uva")
catalogo_precios = {}
for producto in productos_tupla:
    catalogo_precios[producto] = random.randint(10, 100)
print(F"===PRECIOS INICIALES: {catalogo_precios}===\n")
for producto, precio in catalogo_precios.items():
    if precio > 50:
        catalogo_precios[producto] += precio * 0.15
        catalogo_precios[producto] = math.ceil(catalogo_precios[producto])
print(f"precios finales con inpuesto y redondeo): {catalogo_precios}")
precios_finales_unicos = set(catalogo_precios.values())
print(f"precios finales únicos: {precios_finales_unicos}")

