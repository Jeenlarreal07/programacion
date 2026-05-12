'''Simulador de Retorno de Inversión 📈
Enunciado: Simula fluctuaciones diarias en una cuenta de $1000. Si el dinero baja de $500, detén todo de golpe.
Requerimientos: Función con lista de porcentajes. Usa for, asignación (*=), y un if con break. Retorna capital final.'''
def simulador_inversion(flujo_diario):
    capital = 1000
    for porcentaje in flujo_diario:
        capital *= (1 + porcentaje / 100)
        if capital < 500:
            print("¡Alerta! El capital ha bajado de $500. Deteniendo simulación.")
            break
    return capital  
# Ejemplo de uso
fluctuaciones = [5, -3, 2, -10, 4  ] # Lista de fluctuaciones diarias en porcentaje 
resultado = simulador_inversion(fluctuaciones)
print(f"Capital final después de las fluctuaciones: ${resultado:.2f}")  
