
# ejercicio 1

numero = int(input("introduce un numero entero: "))
if numero % 2 == 0:
    print(f"el numero {numero} es par")
else:
    print(f"el numero {numero} es impar")

# ejercicio 2

numero = int(input("introduce un numero:"))
if numero > 0: 
    print("es positivo")
elif numero < 0:
    print("es negativo")
else: 
    print("el numero es neutro")
     
# ejercicio 3

edad = int(input("verifique su mayoria de edad:"))
if 18 <= edad <= 20:
    print("eres mayor de edad")
elif 1 <= edad <=17: 
    print("eres menor de edad")
elif 31 <= edad <= 100:
    print("eres un adulto mayor")
elif 21 <= edad <= 30:
   print("eres un adulto joven")
else:
    print("eres un recien nacido")
    
# ejercicio 4

calificacion = float(input("introduce tu calificacion 0-100:"))
if 60 <= calificacion <= 100:
    print("aprobado")
elif 101 <= calificacion <= 10000000000000000000000:
    print("esta calificacion no existe")
elif -100000000000000000 <= calificacion <= -1:    
    print("esta calificacion no existe")
else:
    print("reprobado")

# ejercicio 5

num1 = float(input("introduce el primer numero:"))
num2 = float(input("introduce el segundo numero:"))
if num1 > num2:
    print(f"el mayor es {num1}")
elif num2 > num1:
    print(f"el mayor es {num2}")
else:
    print("ambos son iguales")
    
# ejercicio 6

compra = float(input("introduce el monto"
" de la compra"))
if compra > 100:
    descuesto = compra * 0.15
    total = compra - descuesto
    print(f"¡tienes el descuesto!"
    f" el total a pagar es: ${total}")
else:
    print(f"no hay descuesto, el total es:" 
        f" ${compra}")
        
# ejercicio 7

dia = int(input("introduce un numero"
                " del 1 al 7:"))
if dia == 1:
    print("lunes")
elif dia == 2:
    print("martes")
elif dia == 3:
    print("miercoles")
elif dia == 4:
    print("jueves")
elif dia == 5:
    print("viernes")
elif dia == 6:
    print("sabado")
elif dia == 7:
    print("domingo")
else:
    print("error")
    
    




