import random
print("===BIENVENIDO A LA LOTERIA===\n")
ganadores_lista = []
while len(ganadores_lista) < 3:
    numero_sorteo = random.randint(1, 10)
    if numero_sorteo not in ganadores_lista:
        ganadores_lista.append(numero_sorteo)
numeros_ganadores = tuple(ganadores_lista)
numeros_usuario = [3, 7, 5]
conjunto_ganadores = set(numeros_ganadores)
conjunto_usuario = set(numeros_usuario)
aciertos_conjuntos = conjunto_ganadores & conjunto_usuario
cantidad_aciertos = len(aciertos_conjuntos)
premio_base = 1000
if cantidad_aciertos == 3:
    premio_final = premio_base * 5
    print(f"¡Felicidades! Has ganado el premio mayor de {premio_final} dólares.")
elif cantidad_aciertos == 2:
    premio_final = premio_base // 2
    print(f"¡Felicidades! Has ganado la mitad del premio mayor, es decir, {premio_final} dólares.")
elif cantidad_aciertos == 1:
    premio_final = 100
    print(f"algo, es algo. Has ganado un premio de consolación de {premio_final} dólares.")
else:
    print("Lo siento, no has ganado ningún premio esta vez. ¡Inténtalo de nuevo!")


print(f"\nNúmeros ganadores: {numeros_ganadores}")
print(f"Números del usuario: {numeros_usuario}")
print(f"Aciertos: {cantidad_aciertos}")