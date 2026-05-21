def clasificar_calificaciones(notas):
    aprobados = 0
    reprobados = 0
    for nota in notas:
        if nota >= 10:
            aprobados += 1
        else:
            reprobados += 1
    return (aprobados, reprobados)
# Ejemplo de uso
notas_estudiantes = [12, 8, 15, 9, 10, 7, 14, 11, 5, 13]
resultado = clasificar_calificaciones(notas_estudiantes)
print(f"Aprobados: {resultado[0]}, Reprobados: {resultado[1]}") 




          
    
 
