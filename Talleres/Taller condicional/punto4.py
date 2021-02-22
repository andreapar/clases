#PUNTO4. Escriba un programa que pida una distancia en centímetros y que escriba esa distancia en kilómetros,
# metros y milimetros (escribiendo todas las unidades).

# #Constantes
MENSAJE_ADIOS = "Adiós, espero buena nota. Gracias"
PREGUNTA_UNO = "Ingrese la distancia en cm: "
PREGUNTA_DOS = "¿A qué unidad la desea convertir? ¿km, m o mm?:"
MENSAJE_DISTANCIA = "La distancia es: "
MENSAJE_OPCION_INVALIDO = "Opción no valida"

#Datos
distancia = float(input(PREGUNTA_UNO))
respuesta_unidad = input(PREGUNTA_DOS)

#Código
if(respuesta_unidad.lower() == "km"):
    distancia = distancia * 10**-5
    print(MENSAJE_DISTANCIA, distancia, "km")
elif(respuesta_unidad.lower() == "m"):
    distancia = distancia * 10**-2
    print(MENSAJE_DISTANCIA, distancia, "m")
elif(respuesta_unidad.lower() == "mm"):
    distancia = distancia * 10
    print(MENSAJE_DISTANCIA, distancia, "mm")
else:
    print( )
print(MENSAJE_ADIOS)