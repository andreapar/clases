#----Constantes----#
PREGUNTA_NOMBRE = "¿Cómo te llamas? : "
PREGUNTA_EDAD = "¿Cuántos años tienes? : "
PREGUNTA_ESTATURA ="¿Cuánto mides? : "
MENSAJE_SALUDO = "un gusto conocerte"

#----Entrada al código----#
nombre = input(PREGUNTA_NOMBRE)
print(MENSAJE_SALUDO, nombre)
input()
edad = int(input(PREGUNTA_EDAD))
estatura = float(input(PREGUNTA_ESTATURA))
