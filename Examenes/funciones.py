from os import system,name

#-----Punto 1-----#

def sumar(a = 0, b = 0, c = 0):
    suma = a + b + c
    return suma

def restar(a = 0, b = 0, c = 0):
    resta = a - b - c
    return resta

def multiplicar(a = 0,b = 0,c = 0):
    multiplica = a * b * c
    return multiplica

def dividir (a = 0,b = 1,c = 1):
    divide = a / b / c
    return divide

def potenciar (base = 0, exponente1 = 1):
    potencia = base ** exponente1
    return potencia


#-----Punto 2 -----#
def mostrarListaMismoTamanho(lista, lista2, lista3):
    if (len (lista) != len(lista2) or len(lista) != len (lista3)):
        print("Las listas no son del mismo tamaño")
        return

    largo = len(lista)
    for indice in range (largo):
        print("Lista 1: ", lista[indice])
        print("Lista 2: ", lista2[indice])
        print("Lista 3: ", lista3[indice])

#---- Punto 3 -----#
def calcularArea(base, altura):
    return (base * altura) / 2

#----- Punto 4 -----#
def mayor(lista):
    return round(max(lista), 2)

def menor(lista):
    return round(min(lista), 2)

def promedio(lista):
    return round(sum(lista) / len(lista), 2)

#----- Punto 5 -----#
def fibonacci(n):
    if n > 0:
        i = 1
        aux = 1
        fib = 0

        while i <= n:
            if i == n:
                print(fib)

            aux = aux + fib 
            fib = aux - fib
            i = i + 1
    

def limpiarPantalla():
    if (name == "nt"):
        _ = system("cls")
    else:
        _ = system("clear")

def pausa():
    input("\n\nPulse la tecla Enter para continuar...")
