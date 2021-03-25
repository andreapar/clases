#----- Sumar dos números -----#
def sumar (a = 0,b = 0):
    '''
        Devuelve la suma de dos números a y b,
        por defecto a vale cero al igual que b
    '''
    suma = a + b
    return suma

#----- Restar dos números -----#
def restar (a = 0,b = 0):
    '''
        Devuelve la resta de dos números a y b,
        por defecto a vale cero al igual que b
    '''
    resta = a - b
    return resta

#----- Multiplicar dos números -----#
def multiplicar (a = 0,b = 0):
    '''
        Devuelve la multiplicación de dos números a y b,
        por defecto a vale cero al igual que b
    '''
    multiplica = a * b
    return multiplica

#----- Dividir dos números -----#
def dividir (a = 0,b = 1):
    '''
        Devuelve la divisón de dos números a y b,
        por defecto a vale cero y b vale uno
    '''
    divide = a / b
    return divide

#----- Potencial de números -----#
def potenciar (base = 0,exponente = 1):
    '''
        Devuelve la potencia de una base y exponente
        por defecto la base vale cero y el exponente 
        vale uno
    '''
    potencia = base ** exponente
    return potencia

#----- Funciones dependientes de otras -----#
def calcular (operacion, numeroA, numeroB):
    '''
        Devuelve el cálculo de dos números a y b,
        con respecto a la operación que se de
    '''
    print(operacion(numeroA,numeroB))

def mostrarLista(lista):
    for elemento in lista:
        print(elemento)

def mostrar2Lista(lista1,lista2):
    for i in range(len(lista1)):
        print(lista1[i], "\t", lista2[i])