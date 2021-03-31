#----- Punto 1 -----#
def mostrarLista (lista):
    for elemento in lista:
        print(elemento)

ciudades = ["Medellín", "Lisboa", "Ámsterdam", "Berlín","Cartagena", "Manizales"]
materias = ["Geografía", "Historia", "Arte", "Música", "Química"]
mostrarLista(ciudades)
print("================================")
mostrarLista(materias)

#----- Punto 2 -----#
listaNumeros = [133,453,768,982,111,279,828]
mayor = max(listaNumeros)
menor = min(listaNumeros)
promedio = round(sum(listaNumeros)/len(listaNumeros))

print("=================================")
print("El número más grande es:", mayor)
print("El número menor es:", menor)
print("El promedio es:", promedio)
print("=================================")

#----- Punto 3 -----#
def saludar (cantidad = 0):
    print( "Hola, " * cantidad)
saludar(11)
print("=================================")

#----- Punto 4 -----#
def listaPares (lista):
    pares = []
    for elemento in lista:
        if (elemento % 2 == 0):
            pares.append(elemento)
    return pares

ListaA = [6, 19, 54, 44, 23,78,80,103,32,3]
numerosPares = listaPares(ListaA)
print(numerosPares)
print("=================================")

#----- Punto 5 -----#
def listaMayor (lista):
    numerosMayor = []
    for elemento in lista:
        if elemento > 24:
            numerosMayor.append(elemento)
    return numerosMayor

ListaC = [56,23,44,77,24,98,97,2,11,75]
numeroALto = listaMayor(ListaC)
print(numeroALto)
print("=================================")

#----- Punto 6 -----#
def IMC (peso, estatura):
    return peso/(estatura ** 2)
calcularImc = IMC(52,1.65)
print(calcularImc)
print("=================================")

#----- Punto 7 -----#
def despedida ():
    print("Feliz día, hasta pronto")
despedida()
