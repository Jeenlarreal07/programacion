def validar_contraseña(contraseña):
    if len(contraseña) > 8 and '@' in contraseña:
        return True
    else:
        return False
# Ejemplo de uso
contraseña = "soyjeen_andry@123" # Contraseña a validar
es_valida = validar_contraseña(contraseña)  
print(f"¿La contraseña es válida? {es_valida}") 

