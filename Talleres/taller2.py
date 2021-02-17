#Constantes
TITULO_BIENVENIDOS ="Hola, hoy haremos operaciones\n"
MENSAJE_DESPEDIDA = "Adiós, gracias"
TITULO_SUMA = "Operación suma: "
TITULO_RESTA = "Operación resta: "
TITULO_MULTIPLICACION = "Operación multiplicacion: "
TITULO_DIVISÓN = "Operación division: "
TITULO_EXPONENTE = "Operación exponente: "

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
resultadoSuma =numA + numB
print(TITULO_SUMA numA, " + ", numB, " = ", resultadoSuma)


