num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))  
operacion = input("Ingrese la operación a realizar (suma, resta, multiplicación, división): ").upper()  
if operacion == "S":
    suma = num1 + num2
    print(f"El resultado de la suma es: {suma}") 
elif operacion == "R":
    resta = num1 - num2
    print(f"El resultado de la resta es: {resta}")       
elif operacion == "M":
    multiplicacion = num1 * num2
    print(f"El resultado de la multiplicación es: {multiplicacion}")     
elif operacion == "D":
    if num2 != 0:
        division = num1 / num2
        print(f"El resultado de la división es: {division}") 
    else:
        print("Error: No se puede dividir por cero.")       
else:    print("Operación no válida. Por favor, ingrese una operación correcta.")   