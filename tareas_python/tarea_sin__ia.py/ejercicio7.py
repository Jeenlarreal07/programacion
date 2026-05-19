estudiantes = {
    "camilo":[14, 16, 18],
    "camila":[19, 20, 18],
    "maria":[10, 12, 11]
}    
for nombre, lista_notas in estudiantes.items():
    promedio = sum(lista_notas) / len(lista_notas)
    print(f"estudiante: {nombre} | promedio: {round(promedio, 2)}")
