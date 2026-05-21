def contar_vocales(frase):
    vocales = 'aeiouAEIOU'
    contador = 0
    for caracter in frase:
        if caracter in vocales:
            contador += 1
    return contador
# Ejemplo de uso
frase = "soy jeen" # Frase a analizar 
resultado = contar_vocales(frase)
print(f"La frase tiene {resultado} vocales.")   


