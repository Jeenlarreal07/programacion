def calcular_suscripciones(precio_mensual, meses):
    total = precio_mensual * meses
    if meses >= 6:
        descuento = total * 0.15
        total -= descuento
        print(f"Descuento aplicado: ${descuento:.2f}")
    else:
        print("No se aplica descuento.")    
    return total
# Ejemplo de uso
precio_mensual = 10 # Precio mensual
meses = 6 # Número de meses     
total_a_pagar = calcular_suscripciones(precio_mensual, meses)
print(f"Total a pagar: ${total_a_pagar:.2f}")

      
  