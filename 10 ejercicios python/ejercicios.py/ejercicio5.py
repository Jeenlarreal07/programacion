"""Conversor y Filtro de Masas ⚖️
Enunciado: Convierte una lista de pesos de gramos a kilogramos. Descarta los que pesen estrictamente menos de 0.585kg.
Requerimientos: Función con lista flotante. Bucle for, divide entre 1000 y usa if para filtrar. Retorna lista nueva."""
def convertir_y_filtrar_pesos(pesos_gramos):
    pesos_kilogramos = []
    for peso in pesos_gramos:
        peso_kg = peso / 1000
        if peso_kg >= 0.585:
            pesos_kilogramos.append(peso_kg)
    return pesos_kilogramos
# Ejemplo de uso
pesos_gramos = [500, 600, 700, 800, 900] # Lista de pesos en gramos
resultado = convertir_y_filtrar_pesos(pesos_gramos) 
print(f"Pesos convertidos a kilogramos y filtrados: {resultado}")   
