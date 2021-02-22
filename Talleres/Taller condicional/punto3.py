from datetime import date
#PUNT03. Escriba un programa que pida el año actual y un año cualquiera
# y que escriba cuántos años han pasado desde ese año o cuántos años faltan para llegar a ese año.

#Constantes
PREGUNTA_ANHO = "Ingresa un año: "
MENSAJE_ANHOS_FALTANTES = "Faltan {} años para el año que ingresaste"
MENSAJE_ANHOS_PASADOS = "Desde el año actual, han pasado {} años"
MENSAJE_ANHOS_IGUALES = "El año ingresado es igual al año actual"

#Datos
anhoUsuario = int(input(PREGUNTA_ANHO))
anhoActual = date.today().year

#Código
if (anhoActual > anhoUsuario):
    resta = anhoActual - anhoUsuario
    print(MENSAJE_ANHOS_PASADOS.format(resta))
elif (anhoActual < anhoUsuario):
    restapasados = anhoUsuario - anhoActual
    print(MENSAJE_ANHOS_FALTANTES.format(restapasados))
else:
    print(MENSAJE_ANHOS_IGUALES)
input()