# TITULO DEL JUEGO
print("bienvenido al juego:".upper())
print("La busqueda del"
  " tesoro perdido…\n")
print("llegas a una isla civilizada"
" llamada los Esqueletos. Frente a ti hay tres caminos.")
print("¿hacia donde quieres ir?")
opcion1 = input("(SELVA / CUEVA / ACANTILADO): ").lower()
if opcion1 == "selva":
    print("¡Bien! Te adentras en la selva."
    " Tras caminar horas, llegas a un RÍO con cocodrilos.")
    
# nivel 2 de selva:
    
    opcion2 = input("¿Que decides hacer?"
" (NADAR / PUENTE / RODEAR): ").lower()
    if opcion2 == "puente":
        print("El tronco es inestable,"
    " pero logras cruzar."
    " Al otro lado ves un TEMPLO antiguo.")
    elif opcion2 == "nadar":
        print("Los cocodrilos son más"
     " rápidos que tú. GAME OVER.")
    elif opcion2 == "rodear":
        print("Caminas demasiado,"
" te desorientas y te pierdes en las"
" profundidades de la selva. GAME OVER.")
    else:
       print("respuesta no valida,"
              " GAME OVER.")
# Nivel 3 de la selva:
elif opcion1 == "cueva":
    print("Entras en una cueva oscura."
" Te refugias por una noche"
 " y al despertar te encuentras"
   " rodeado de serpientes")
    
# nivel 2 de cueva:
    
    opcion2 = input("¿Que decides hacer?"
" (COMERLAS / NADA / correr):").lower()
    if opcion2 == "comerlas":
        print("¡GRAN ERROR! moriste"
" por bacterias. GAME OVER")
    elif opcion2 == "nada":
        print("¡GRAN ERROR! te terminaron"
" mordiendo por no actuar rapido")
    elif opcion2 == "correr":
        print("¡hiciste lo correcto!"
 " fuiste rapido y saliste de la cueva,"
" al salir te das cuenta que la"
" isla esta repleta de animales peligrosos")
    else:
        print("respuesta no valida,"
               " GAME OVER.")
# nivel 3 de la cueva:
 
        opcion3 = input("¿Que decides hacer ahora?"
    " (SEGUIR / retirarte / FRUSTRARTE:) ").lower()
        if opcion3 == "seguir":
            print("te adentras a las profundidades"
    " de la isla y te mata una pantera. GAME OVER")
        elif opcion3 == "retirarte":
            print("¡EXCELENTE! priorizas"
    " tu vida y vuelves al inicio"
    " de la isla para regresar a casa. haz"
    " perdido el juego pero has salido con vida")
        elif opcion3 == "frustrarte":
            print("no logras nada y"
    " no haces nada por ti. te vuelves"
    " presa de los animales por"
    " no actuar rapido. GAME OVER.")
        else:
            print("respuesta no valida,"
                   " GAME OVER.")
# FIN DEL NIVEL CUEVA.

elif opcion1 == "acantilado":
    print("Subes por las rocas."
    " El viento sopla fuerte y"
" ves toda la isla desde arriba, de repente"
" te encuentras con un tigre")
else:
    print("respuesta no valida,"
           " GAME OVER.")
# nivel 2 de acantilado
opcion2 = input("¿Que decides hacer?"
" (DEFENDERTE / BAJAR / CALMARTE:) ").lower()
if opcion2 == "defenderte":
    print("atacas al tigue pero"
        " el es mucho mas fuerte que tú."
        " GAME OVER.")
elif opcion2 == "bajar":
    print("bajas el acantilado pero"
        " te resbalas y mueres. GAME OVER")
elif opcion2 == "calmarte":
    print("mantienes la calma y el"
        " tigre no entra en defensa,"
        " solo te observa y se va.")
else:
    print("respuesta no valida,"
               " GAME OVER.")
# nivel 3 de acantilado

opcion3 = input("Tras el susto,"
    " ves una cueva brillante y" 
    " un sendero que baja. ¿Que haces?"
    " (EXPLORAR / VOLVER A CASA / GRITAR): ").lower()
if opcion3 == "explorar":
    print("¡INCREIBLE! Dentro de la cueva"
        " brillante encuentras el tesoro "
 "de los Esqueletos. ¡HAS GANADO EL JUEGO!")
elif opcion3 == "volver a casa":
    print("Decides no arriesgarte mas"
 " y vuelves a casa. Estas a salvo, pero el"
 " tesoro sigue alli en esa isla. FIN.")
elif opcion3 == "gritar":
    print("Tu grito provoca un pequeño derrumbe de rocas. "
            "Quedas atrapado en la cima sin salida. GAME OVER.")
else:
    print("respuesta no valida,"
                   " GAME OVER.")
    
        
      
