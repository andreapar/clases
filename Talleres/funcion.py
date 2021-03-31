#----- Punto 1-----#
def mostrarLista (lista):
    for elemento in lista:
        print(elemento)

#----- Punto 2 -----#
def mostrarEstadistica (lista):
    mayor = max lista
    menor = min lista
    promedio = round(sum(lista)/len(lista),2)

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
def listaMayor (lista):
    numerosMayor = []
    for elemento in lista:
        if elemento > 24:
            numerosMayor.append(elemento)
    return numerosMayor

#----- Punto 6 -----#
def calcularImc (peso, estatura):
    return peso/(estatura ** 2)

#----- Punto 7 -----#
def despedida ():
    print("Feliz día, hasta pronto")

