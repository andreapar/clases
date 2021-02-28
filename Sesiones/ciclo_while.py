#Constantes
MENSAJE_BIENVENIDA = "Hola, te ayudaré ahorrando "
PREGUNTA_VALORPC = "¿Cuánto vale el PC que deseas?: "
PREGUNTA_AHORRO = "¿Cuánto dinero tienes ahorrado?: "
MENSAJE_AHORRO = "Llevas ahorrado... "

#Código
print (MENSAJE_BIENVENIDA)
valor = float(input(PREGUNTA_VALORPC))
ahorrado = float(input(PREGUNTA_AHORRO))

while(valor > ahorrado):
    print (MENSAJE_AHORRO, ahorrado, "Te faltan... ", valor - ahorrado)
    ahorrado = ahorrado + 1000
print (valor == ahorrado)