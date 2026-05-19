def analizar_palabras(lista1, lista2):
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    en_ambas = conjunto1 & conjunto2
    exclusivas_primero = conjunto1 - conjunto2
    return en_ambas, exclusivas_primero
grupo1 = ["manzana", "banana", "naranja", "pera"]
grupo2 = ["banana", "kiwi", "naranja", "uva"]
ambas, exclusivas = analizar_palabras(grupo1, grupo2)
print("palabras que estan en ambas listas:", ambas)
print("palabras exclusivas de la primera lista:", exclusivas)
