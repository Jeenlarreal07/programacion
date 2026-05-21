def clasificar_usuarios(usuarios):
    clasificacion = {
        "Activos": [],
        "Por_Vencer": [],
        "Expirados": []
    }
    
    for usuario, dias in usuarios.items():
        if dias > 5:
            clasificacion["Activos"].append(usuario)
        elif 0 < dias <= 5:
            clasificacion["Por_Vencer"].append(usuario)
        else:
            clasificacion["Expirados"].append(usuario)
    
    return clasificacion
# Ejemplo de uso
usuarios = {
    "Alice": 10,
    "Bob": 3,
    "Charlie": 0,
    "David": 7
}
resultado = clasificar_usuarios(usuarios)
for categoria, lista_usuarios in resultado.items():
    print(f"{categoria}: {lista_usuarios}")
 
