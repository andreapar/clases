#Constantes
TITULO_BIENVENIDOS ="Hola, hoy haremos operaciones\n"
MENSAJE_DESPEDIDA = "Adiós, gracias"
TITULO_SUMA = "Operación suma: "
TITULO_RESTA = "Operación resta: "
TITULO_MULTIPLICACION = "Operación multiplicacion: "
TITULO_DIVISION = "Operación division: "
TITULO_EXPONENTE = "Operación exponente: "
TITULO_DIVISION_POR_CERO = "No se puede dividir entre 0"

NUMERO1 = "Por favor digita un número: "
NUMERO2 = "Para continuar, digita otro número: "

print(TITULO_BIENVENIDOS)

# Datos
numeroA = input(NUMERO1)
numeroB = input(NUMERO2)
input()
numA = float (numeroA)
numB = float (numeroB)

#Código
resultadoSuma = numA + numB
print(TITULO_SUMA, numA, " + ", numB, " = ", resultadoSuma)

resultadoResta = numA - numB
print(TITULO_RESTA, numA, " - ", numB, " = ", resultadoResta)

resultadoMultiplicacion = numA * numB
print(TITULO_MULTIPLICACION, numA, " * ", numB, " = ", resultadoMultiplicacion)

if (numB != 0):
    resultadoDivision = numA / numB
    print(TITULO_DIVISION, numA, " / ", numB, " = ", resultadoDivision)
else:
    print(TITULO_DIVISION, TITULO_DIVISION_POR_CERO)

resultadoExponenciacion = numA ** numB
print(TITULO_EXPONENTE, numA, " ^", numB, " =", resultadoExponenciacion)

print("Comparación Mayor, menor e igual")
if (numA > numB):
    print("El número ", numA, " es mayor que ", numB)
elif (numA < numB):
    print("El número ", numA, " es menor que ",numB)
elif (numA == numB):
    print("Los números ", numA, " son iguales")
input()

print(MENSAJE_DESPEDIDA)