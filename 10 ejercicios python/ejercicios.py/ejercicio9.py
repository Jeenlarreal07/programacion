''''Rastreador de Frases Clave 🔍
Enunciado: Extrae de una lista de diálogos solo las oraciones que digan "Valar Morghulis", sin importar mayúsculas.
Requerimientos: Función con lista. Bucle for, usa .lower() y el operador in en una condicional.'''
def rastreador_frases_clave(dialogos):
    frases_clave = []
    for dialogo in dialogos:
        if "valar morghulis" in dialogo.lower():
            frases_clave.append(dialogo)
    return frases_clave 
# Ejemplo de uso
dialogos = [
    "Valar Morghulis",   
    "valar morghulis",
    "VALAR MORGHULIS",      
    "Valar Dohaeris",
    "No es lo que parece"
] # Lista de diálogos   
resultado = rastreador_frases_clave(dialogos)
print("Frases clave encontradas:")  
for frase in resultado:
    print(frase)    