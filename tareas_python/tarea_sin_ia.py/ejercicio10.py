inventario = {
    "manzanas": 10,
    "platanos": 5,
    "huevos": 3
}
while True:
    print("\n--- Inventario actual: ---")
    print(inventario)
    producto = input(" ¿qué producto quieres comprar? (o presiona 'salir' si no estas interesad@): ").lower()
    if producto == "salir":
        print("¡Gracias por usar nuestro sistema!")
        break
    elif producto in inventario:
        cantidad = int(input(f"¿Cuántas unidades de {producto} quieres comprar?"))
        if inventario[producto] >= cantidad:
            inventario[producto] -= cantidad
            print(f"¡venta exitosa! has comprado {cantidad} {producto}.")
        else:
            print(f"error, no hay suficiente stock. Solo nos queda: {inventario[producto]}")     
else:
    print("error, el producto no esta en el inventario.")       


