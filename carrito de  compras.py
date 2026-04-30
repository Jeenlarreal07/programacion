cesta = [("Manzanas", 2.50), ("Pan", 1.75), ("Leche", 3.00), ("Huevos", 2.25), ("Queso", 4.50), ("Yogur", 2.00)]
def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Agregar un nuevo elemento")
    print("2. Mostrar el contenido de la cesta de la compra")
    print("3. Eliminar un elemento")
    print("4. Calcular el total de la compra")
    print("5. Renunciar")   
def agregar_elemento():
    elemento = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cesta.append((elemento, precio))
    print(f"{elemento} ha sido agregado a la cesta con un precio de ${precio:.2f}.")        
def mostrar_cesta():
    if not cesta:
        print("La cesta de la compra está vacía.")
    else:
        print("Contenido de la cesta de la compra:")
        for i, (elemento, precio) in enumerate(cesta, start=1):
            print(f"{i}. {elemento} - ${precio:.2f}")   
def eliminar_elemento():
    mostrar_cesta()
    if cesta:
        indice = int(input("Ingrese el número del producto a eliminar: "))
        if 1 <= indice <= len(cesta):
            eliminado = cesta.pop(indice - 1)
            print(f"{eliminado[0]} ha sido eliminado de la cesta.")
        else:
            print("Número inválido. Por favor, intente nuevamente.")
def calcular_total():
    total = sum(precio for _, precio in cesta)
    print(f"El total de la compra es: ${total:.2f}")    
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-5): ")
    if opcion == "1":
        agregar_elemento()
    elif opcion == "2":
        mostrar_cesta()
    elif opcion == "3":
        eliminar_elemento()
    elif opcion == "4":
        calcular_total()
    elif opcion == "5":
        print("Gracias por usar el programa de gestión de la cesta de compras. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 5.") 
