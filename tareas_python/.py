colores = ("verde", "rojo", "amarillo")
while True:
    print("BIENVENIDO AL SEMAFORO.\n")
    colores = input("que color eliges? verde, rojo o amarillo\n (o salte del sistema presionando 'salir'): ").lower()
    if colores == "salir":
        break
    elif colores == "verde":
        print("si")
    elif colores == "rojo":
        print("yes")
    elif colores == "amarillo":
        print("amarillo")
    else:
        print("no")
        

       

    