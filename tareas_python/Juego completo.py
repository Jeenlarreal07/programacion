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
    
# nivel 1 de selva:
    
    opcion2 = input("¿Que decides hacer?"
" (NADAR / PUENTE / RODEAR): ").lower()
    if opcion2 == "puente":
        print("El tronco es inestable,"
    " pero Logras cruzar y llegas a la entrada"
    " de un TEMPLO antiguo cubierto de vegetación")
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
# Nivel 2 de la selva:
       opcion2 = input("La entrada del templo"
        " está bloqueada por tres puertas de piedra"
        " con grabados antiguos. ¿Cuál decides abrir?" 
        " SOL / LUNA / ESTRELLA): ").lower()
       if opcion2 == "sol":
           print("La puerta se desliza hacia"
            " arriba y revela un pasillo iluminado"
            " por antorchas de fuego eterno.")
       elif opcion2 == "estrella":
           print("Un gas somnífero sale de"
           " la puerta y te desmayas."
           " Despiertas horas después en la"
           " playa donde empezaste TOTAL TIEMPO PERDIDO."
           " GAME OVER.")
       elif opcion2 == "luna":
           print("Al tocarla, el suelo desaparece"
           " y caes en un pozo sin fondo."
           " GAME OVER.")
# nivel 3 de la selva
       opcion3 = input("El pasillo tiene baldosas"
           " con dibujos de animales."
           " ¿Cuál pisas para avanzar? (SERPIENTE / AGUILA / JAGUAR): ").lower()
       if opcion3 == "serpiente":
           print("Activas dardos venenosos. GAME OVER")
       elif opcion3 == "aguila":
            print("La baldosa es segura y una puerta se abre.")
       elif opcion3 == "jaguar":
            print("El techo empieza a bajar lentamente hasta matarte."
                " GAME OVER.")
# nivel 4 de la selva
       opcion4 = input("Llegas a un altar"
            " con tres objetos antiguos."
            " Una voz dice: Solo uno te permitirá ver al Guardián. ¿Cuál tomas?"
            " (CALIZ / DAGA / MASCARA):").lower()
       if opcion4 == "caliz":
           print("Bebes de el y recuperas fuerzas")
       elif opcion4 == "daga":
           print("Es una trampa; la sala se sella. GAME OVER.")
       elif opcion4 == "mascara":
           print("Te la pones y quedas cegado. GAME OVER.")
# nivel 5 de la selva
       opcion5 = input("Un gigante de piedra te bloquea"
       " el paso. El gigante te pregunta cual es tu mejor virtud."
       " ¿Qué respondes? ( FUERZA / SABIDURIA / VALOR):").lower()
       if opcion5 == "fuerza":
           print("El espíritu te desafía a un duelo y"
           " te derrota fácilmente. GAME OVER.")
       elif opcion5 == "sabiduria":
           print("Te hace una pregunta técnica sobre"
           " la isla y, al responder bien, se aparta")
       elif opcion5 == "valor":
           print("Te lanza una llamarada"
           " para probar tu miedo; no la esquivas"
           " y te quemas. GAME OVER.")
# nivel final de la selva
       opcion6 = input("Estás frente al Tesoro de los Esqueletos."
       " El espíritu te pide que decidas el destino del oro."
       " ¿ Que destino eliges ? (DONAR / QUEMAR / REINAR):").lower()
       if opcion6 == "donar":
           print("Lo usaré para construir escuelas"
           " y hospitales. El cofre se abre y te transportas"
           " a casa con riquezas. ¡HAS GANADO EL JUEGO!")
       elif opcion6 == "quemar":
           print("Nadie debería tener tanto poder,"
           " destruiré el tesoro. El espíritu te felicita"
           " por tu ética y te deja ir en paz, pero pobre. FIN")
       elif opcion6 == "reinar":
           print("Usaré el oro para comprar un ejército"
           " y gobernar la isla. El espíritu te encierra"
           " en un sarcófago por tu ambición. GAME OVER")

# nivel 1 de la cueva

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
# NIVEL 2 de acantilado

elif opcion1 == "acantilado":
    print("Subes por las rocas."
    " El viento sopla fuerte y"
" ves toda la isla desde arriba, de repente"
" te encuentras con un tigre")
else:
    print("respuesta no valida,"
           " GAME OVER.")
# nivel 3 de acantilado
    opcion7 = input("¿Que decides hacer?"
" (DEFENDERTE / BAJAR / CALMARTE:) ").lower()
    if opcion7 == "defenderte":
        print("atacas al tigue pero"
        " el es mucho mas fuerte que tú."
        " GAME OVER.")
    elif opcion7 == "bajar":
        print("bajas el acantilado pero"
        " te resbalas y mueres. GAME OVER")
    elif opcion7 == "calmarte":
        print("mantienes la calma y el"
        " tigre no entra en defensa,"
        " solo te observa y se va.")
    else:
        print("respuesta no valida,"
               " GAME OVER.")
               
# FIN DEL NIVEL DEL ACANTILADO

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
    
        
      
