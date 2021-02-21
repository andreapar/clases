#PUNTO 1
#Constantes
MENSAJE_ENTRADA = "Hola, profe espero que estés bien"
MENSAJE_ADIOS = "Adiós, espero buena nota"
NUMERO1 = "Por favor digita un número: "
NUMERO2 = "Para continuar, digita otro número: "

print("========================================")
print(MENSAJE_ENTRADA)
print("========================================")
# Datos
numeroA = input(NUMERO1)
numeroB = input(NUMERO2)
input()
numA = float (numeroA)
numB = float (numeroB)

#Código
print("Comparación mayor, menor e igual")
if (numA > numB):
    print("El número ", numA, " es mayor que ", numB)
elif (numA < numB):
    print("El número ", numA, " es menor que ",numB)
else:
    print("Los números ", numA, " son iguales")
input()

#PUNTO2 
#Constantes
PREGUNTA_EDAD = "Por favor ingresa tu edad: "
MENSAJE_MENOR_EDAD = "Todavía tienes mucho por delante"
MENSAJE_JOVEN = "Espero que estés feliz"
MENSAJE_ADULTO = "Recuerda, el trabajo no es todo"
MENSAJE_ADULTO_MAYOR = "Haz tenido una vida linda"

#Código
edad = int(input(PREGUNTA_EDAD))
isMenorEdad = edad <18
isJoven = edad >= 18 and edad < 25
isAdulto = edad >= 26 and edad < 60
isMayorAdulto = edad >= 60
resultado = ""

if(isMenorEdad):
    resultado = MENSAJE_MENOR_EDAD
elif(isJoven):
    resultado = MENSAJE_JOVEN
elif(isAdulto):
    resultado = MENSAJE_ADULTO
else:
    resultado = MENSAJE_ADULTO_MAYOR

print(resultado)
input()

#PUNTO3
#Constantes
PREGUNTA_AÑO_ACTUAL = "Por favor, ingrese el año actual: "
PREGUNTA_AÑO = "Ingresa un año: "
MENSAJE_AÑOS_FALTANTES = "Faltan {} años para el año que ingresaste"
MENSAJE_AÑOS_PASADOS ="Desde el año actual, han pasado {} años"

#Datos
añoA = int(input(PREGUNTA_AÑO_ACTUAL))
añoActual = int(input(PREGUNTA_AÑO))

#Código
if(añoActual > añoA):
    resta = añoActual - añoA
    print(MENSAJE_AÑOS_PASADOS.format(resta))
elif(añoActual < añoA):
    restapasados = añoA - añoActual
    print(MENSAJE_AÑOS_FALTANTES.format(restapasados))
else:
    print("Los años que ingresantes son iguales")
input()

#PUNTO4
#Constantes
