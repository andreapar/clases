#Pregunta 1

#Constantes
MENSAJE_BIENVENIDA = "Hola, profe espero que estés bien"
MENSAJE_DESPEDIDA = "Adiós, espero buena nota"
NUMERO1 = "Por favor digita un número: "
NUMERO2 = "Para continuar, digita otro número: "

print(MENSAJE_BIENVENIDA)
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
print (MENSAJE_DESPEDIDA)


