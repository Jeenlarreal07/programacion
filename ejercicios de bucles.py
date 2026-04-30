'''1. Acumulador con interrupción ➕
Enunciado: Desarrollar un programa que pida números enteros para sumarlos. El programa debe detenerse y mostrar el resultado total SOLAMENTE cuando se ingrese un 0.
Requerimientos: 
- Usar bucle while.
- Usar break para salir con el 0.'''

# EJERCICIO 1: Acumulador con interrupción ➕
total = 0
while True:
    numero = int(input("Ingrese un número entero (0 para finalizar): "))
    if numero == 0:
        break
    total += numero
print(f"La suma total es: {total}") 


''' EJERCICIO 2: Saltando múltiplos 🦘
Enunciado: Imprimir los números del 1 al 20, saltándose todos los que sean múltiplos de 3.
Requerimientos: 
- Usar bucle for y range().
- Usar continue para evitar imprimir los múltiplos.'''
# EJERCICIO 2: Saltando múltiplos 🦘
for i in range(1, 20):
    if i % 3 == 0:
        continue
    print(i)            
''' EJERCICIO 3: Verificador de números primos 🔢
Enunciado: Pedir un número entero y determinar si es primo.
Requerimientos: 
- Iterar con un for.
- Usar break al encontrar un divisor.
- Aprovechar la estructura for...else de Python.'''

# EJERCICIO 3: Verificador de números primos 🔢
numero = int(input("Ingrese un número entero: "))
if numero < 2:
    print(f"{numero} no es un número primo.")
else:
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            print(f"{numero} no es un número primo.")
            break
    else:
        print(f"{numero} es un número primo.")  

''' EJERCICIO 4: Simulador de acceso 🔐
Enunciado: Crear un login con contraseña ("python123"). El usuario tiene solo 3 intentos.
Requerimientos: 
- Usar while con contador.
- Salir con break si la contraseña es correcta, de lo contrario, bloquear al tercer intento fallido.'''
# EJERCICIO 4: Simulador de acceso 🔐

contraseña_correcta = "python123"
intentos = 0
while intentos < 3:
    contraseña_ingresada = input("Ingrese la contraseña: ")
    if contraseña_ingresada == contraseña_correcta:
        print("¡Acceso concedido!")
        break
    else:
        intentos += 1
        print(f"Contraseña incorrecta. Intento {intentos} de 3.")   
if intentos == 3:
    print("Has sido bloqueado por demasiados intentos fallidos.")   
