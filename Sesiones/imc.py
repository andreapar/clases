#----Constantes----#
PREGUNTA_PESO = "¿Cuánto pesas en kg? : "
PREGUNTA_ESTATURA = "¿Cuánto mides en mts? : "
MENSAJE_BIENVENIDA = "Hola, ¿cómo estas? Voy a calcular tu IMC"
MENSAJE_DESPEDIDA = "Tu IMC es ..."

#----Entrada código----#
print(MENSAJE_BIENVENIDA)
peso = float (input(PREGUNTA_PESO))
estatura = float(input(PREGUNTA_ESTATURA))
imc = peso/(estatura**2)
print(MENSAJE_DESPEDIDA,imc)


