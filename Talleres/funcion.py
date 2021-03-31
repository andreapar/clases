from os import system, name

#----- Punto 1-----#
def mostrarLista (lista):
    for elemento in lista:
        print(elemento)

#----- Punto 2 -----#
def mayor (lista):
    return round(max(lista),2)

def menor (lista):
    return round(min(lista),2)

def promedio (lista):
    return round(sum(lista)/len(lista),2)

#----- Punto 3 -----#
def saludar (cantidad = 0):
    print( "Hola, " * cantidad)

#----- Punto 4 -----#
def listaPares (lista):
    pares = []
    for elemento in lista:
        if (elemento % 2 == 0):
            pares.append(elemento)
    return pares

#----- Punto 5 -----#
def listaMayor (lista, valorReferencia):
    numerosMayor = []
    for elemento in lista:
        if elemento > valorReferencia:
            numerosMayor.append(elemento)
    return numerosMayor

#----- Punto 6 -----#
def calcularImc (peso, estatura):
    return peso/(estatura ** 2)

#----- Punto 7 -----#
def despedida ():
    print("Feliz día, hasta pronto")

def limpiarPantalla():
    if (name == "nt"):
        _ = system("cls")
    else:
        _ = system("clear")

def pausa():
    input("\n\nPulse la tecla Enter para continuar...")

