#Constantes
TITULO_HOLAA = "Hola, hoy miraremos tus valores de triglecéridos y homocisteína"
MENSAJE_HASTA_LUEGO = "Adiós,vuelva pronto. Gracias"
MENSAJE_OPTIMO = "Estás en estado optimo, sigue así "
MENSAJE_SOBRE_EL_LIMITE  = "Te encuentras sobre el límite óptimo"
MENSAJE_ALTO = "Estás en lo alto, ten cuidado"
MENSAJE_MUY_ALTO = "Te encuentras en lo más alto, debes preocuparte"
MENSAJE_OPTIMO_HOMOCISTEINA = "Estás en un estado optimo, continua así"
MENSAJE_SOBRE_EL_LIMITE_HOMOCISTEINA  = "Estás sonbre el límite óptimo"
MENSAJE_ALTO_HOMOCISTEINA = "Estás en lo alto, debes cuidarte"
MENSAJE_MUY_ALTO_HOMOCISTEINA = "Te encuentras en lo más alto por favor, preocupate"
PREGUNTA_TRIGLECERIDOS = "Por favor ingrese su valor de triglecéridos: "
PREGUNTA_HOMOCISTEINA = "Para continuar, dígite su valor de homocisteína: "

#Código
print("=========================================================================")
print(TITULO_HOLAA)
print("==========================================================================")
trigleceridos = int(input(PREGUNTA_TRIGLECERIDOS))
isOptimo = trigleceridos < 150
isSobreOptimo = trigleceridos >= 150 and trigleceridos < 199
isAlto = trigleceridos >= 200 and trigleceridos < 499
isMuyAlto = trigleceridos >= 500

if (isOptimo):
    print(MENSAJE_OPTIMO)
elif (isSobreOptimo):
    print(MENSAJE_SOBRE_EL_LIMITE)
elif (isAlto):
    print(MENSAJE_ALTO)
else:
    print(MENSAJE_MUY_ALTO)

homocisteina = int(input(PREGUNTA_HOMOCISTEINA))
isOptimo = homocisteina >= 2 and homocisteina < 14
isSobreOptimo = homocisteina >= 15 and homocisteina < 29
isAlto = homocisteina >= 30 and homocisteina < 99
isMuyAlto = homocisteina >=100

if (isOptimo):
    print(MENSAJE_OPTIMO_HOMOCISTEINA)
elif (isSobreOptimo):
    print(MENSAJE_OPTIMO_HOMOCISTEINA)
elif (isAlto):
    print(MENSAJE_ALTO_HOMOCISTEINA)
else:
    print(MENSAJE_MUY_ALTO_HOMOCISTEINA)
input()

print("Gracias por participar")


