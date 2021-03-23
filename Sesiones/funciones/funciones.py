#----- Sumar dos números -----#
def sumar (a = 0,b = 0):
    suma = a + b
    return suma

#----- Restar dos números -----#
def restar (a = 0,b = 0):
    resta = a - b
    return resta

#----- Multiplicar dos números -----#
def multiplicar (a = 0,b = 0):
    multiplica = a * b
    return multiplica

#----- Dividir dos números -----#
def dividir (a = 0,b = 1):
    divide = a / b
    return divide

#----- Potencial de números -----#
def potenciar (base = 0,exponente = 1):
    potencia = base ** exponente
    return potencia

#----- Funciones dependientes de otras -----#
def calcular (operacion, numeroA, numeroB):
    print(operacion(numeroA,numeroB))