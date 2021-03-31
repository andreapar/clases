#----- Punto 1-----#
def mostrarLista (lista):
    for elemento in lista:
        print(elemento)

#----- Punto 2 -----#
def mostrarEstadistica (lista):
    mayor = round(max(lista),2)
    menor = round(min(lista),2)
    promedio = round(sum(lista)/len(lista),2)
    print("El número más grande es:", mayor)
    print("El número menor es:", menor)
    print("El promedio es:", promedio)

#----- Punto 5 -----#
def saludar (cantidad = 0):
    print( "Hola, " * cantidad)

#----- Punto 3 -----#
def listaPares (lista):
    pares = []
    for elemento in lista:
        if (elemento % 2 == 0):
            pares.append(elemento)
    return pares

#----- Punto 4 -----#
def listaMayor (lista):
    numerosMayor = []
    for elemento in lista:
        if elemento > 24:
            numerosMayor.append(elemento)
    return numerosMayor

#----- Punto 6 -----#
def calcularImc (peso, estatura):
    return peso/(estatura ** 2)
    print(calcularImc(peso,estatura))

#----- Punto 7 -----#
def despedida ():
    Adios = ()
    print("Feliz día, hasta pronto")

