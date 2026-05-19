import random
lista_aleatoria = []
lista_pares = []
lista_impares = []
for i in range(15):
    lista_aleatoria.append(random.randint(1, 50))
for numero in lista_aleatoria:
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
            lista_impares.append(numero)
print(f"la lista de numeros aleatorios es:{lista_aleatoria}")
print(f"la lista de numeros pares es:{lista_pares}")
print(f"la lista de numeros impares es:{lista_impares}")