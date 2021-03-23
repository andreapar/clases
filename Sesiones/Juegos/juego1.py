#Entradas
MENSAJE_SALUDO = "Bienvenido al juego"
PREGUNTA_NUMERO = '''
        En este juego debes acertar un número
        que va desde el 1 al 10, la idea es que
        lo puedes intentar las veces que quieras
        ¡Suerte!
        Ingresa tú número: '''
PREGUNTA_FALLASTE = " Fallaste, ingresa otro número: "
MENSAJE_GANASTE = "Felicidades, ganaste"
MENSAJE_PERDIDA = "Perdiste, intenta de nuevo"
DESPEDIDA = "Adióss"

#Código
numOcul = 5
vidas = 3

print (MENSAJE_SALUDO)
numIngresado = int(input(PREGUNTA_NUMERO))
if (numOcul != numIngresado):
    vidas = vidas -1
while (numOcul != numIngresado and vidas > 0):
    numIngresado = int(input(PREGUNTA_FALLASTE))
    vidas = vidas -1

if (vidas >= 0 and numOcul == numIngresado):
    print (MENSAJE_GANASTE)
    print (vidas)
else:
    print (MENSAJE_PERDIDA, ", el número era el",numOcul)

print (DESPEDIDA)






