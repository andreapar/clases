import random

#Entrada

MENSAJE_SALUDAR = "Bienvenido al juego"
PREGUNTAR_NUMERO = '''
        En este juego debes acertar un número
        que va desde el 1-10, la idea es que
        lo puedes intentar antes de que se te
        acaben las vidas.
        ¡Suerte!
        Ingresa tú número: 
'''
PREGUNTA_DIFICULTAD = '''
    1. Fácil
    2. Moderado
    3. Difícil
'''
PREGUNTA_FALLIDA = " Fallaste :C , ingresa otro número: "
MENSAJE_GANAR = "¡Felicidades, ganaste!"
MENSAJE_PERDISTE = "Perdiste, vueve a intertanrlo"
DESPEDIDA = "Adióss"

#Datos
numeroOculto = random.randint(1,10)
vidas = None

#Código
print(MENSAJE_SALUDAR)
dificultad = int(input(PREGUNTA_DIFICULTAD))
while (dificultad != 1 and dificultad != 2 and dificultad != 3):
    print ("Ingresa una opciób válida")
    dificultad = int(input(PREGUNTA_DIFICULTAD))

if (dificultad == 1):
    print("Modo fácil activado")
    vidas = 5
elif (dificultad == 2):
    print("Modo moderado activado")
    vidas = 3
else:
    print("Modo difícil activado")
    vidas = 1

numeroIngresado = int(input(PREGUNTAR_NUMERO))
while (numeroIngresado != numeroOculto and vidas > 1):
    vidas = vidas -1
    print(f"Te quedan {vidas} vidas")
    numeroIngresado = int(input(PREGUNTA_FALLIDA))

if (vidas >= 0 and numeroIngresado == numeroOculto):
    print (MENSAJE_GANAR)
else:
    print(MENSAJE_PERDISTE, "El número era el ", numeroOculto)
