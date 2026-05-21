def procesar_transacciones(transacciones):
    saldo_final = 0
    gasto_maximo = 0
    total_ingresos = 0
    contador_ingresos = 0
    
    for transaccion in transacciones:
        if transaccion > 0:  # Ingreso
            saldo_final += transaccion
            total_ingresos += transaccion
            contador_ingresos += 1
        elif transaccion < 0:  # Egreso
            saldo_final += transaccion
            if abs(transaccion) > gasto_maximo:
                gasto_maximo = abs(transaccion)
    
    promedio_ingresos = total_ingresos / contador_ingresos if contador_ingresos > 0 else 0
    
    return {
        "saldo_final": saldo_final,
        "gasto_maximo": gasto_maximo,
        "promedio_ingresos": promedio_ingresos
    }
# Ejemplo de uso
transacciones = [1000, -200, 500, -300, 1500, -100]
resultado = procesar_transacciones(transacciones)
print(f"Saldo final: {resultado['saldo_final']}")
print(f"Gasto máximo: {resultado['gasto_maximo']}")
print(f"Promedio de ingresos: {resultado['promedio_ingresos']}")

