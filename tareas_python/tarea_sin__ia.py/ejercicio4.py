import random
numero_secreto = random.randint(1, 10)
print("¡Bievenidos al juego! Intenta adivinar el numero del 1 al 10. Tienes 3 intentos.")
for intento in range(3):
    suposicion = int(input("Introduce tu numero:"))
    if suposicion == numero_secreto:
        print("¡Felicidades, Has ganado!")
        break
else:
    print("Lo siento. Se agotaron tus intentos.")
print(f"\nEl numero secreto era: {numero_secreto}. ¡Gracias por jugar!")