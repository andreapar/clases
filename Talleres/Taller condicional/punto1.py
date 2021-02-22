#PUNTO1. Dado dos números determine si son iguales o cual es el mayor

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
numA = float(numeroA)
numB = float(numeroB)

#Código
print("Comparación mayor, menor o igual")
if (numA > numB):
    print("El número ", numA, " es mayor que ", numB)
elif (numA < numB):
    print("El número ", numA, " es menor que ",numB)
else:
    print("Los números ", numA, " son iguales")
input()