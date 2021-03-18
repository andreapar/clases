guardar = print("Hola")
print(guardar)

guardar = round(14.23456,2)
print(guardar)

def linedesign(simbolo = "#", cantidad = 4):
    print(simbolo * cantidad)
    return None

linedesign(30, "#")
linedesign(9,"*")
linedesign()

#----- Muestre la lista -----#
def mostrarLista(listaEntrada = []):
    for elemento in listaEntrada:
        print(elemento)
    return None
lista = [131,151,342,424,21,656]
lista2 = [9979,86,66,99,97,56]
linedesign(4, "(╯°□°)╯" )
mostrarLista(lista)
linedesign(15,"#")
mostrarLista(lista2)

#----- Sumar dos números -----#
def sumar (a = 0,b = 0):
    suma = a + b
    return suma
linedesign(32, "-")
resultado = sumar()
print(resultado)
print(sumar(12,14))
round(12.22333,2)

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

print(restar(83,84))
print(multiplicar(83,84))
print(dividir(83,84))
