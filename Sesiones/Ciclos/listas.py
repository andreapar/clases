nombres = []
print(type(nombres))
print(nombres)
nombres = ["Eren", "Levi", "Mikasa", "Armin"]
print(nombres)
print(nombres [1] )
nombres.append("Erwin")
print(nombres)
print(nombres[2])
print()

edades = [18,19,20,17,32,14,13,16,12,15]
estaturas = [1,62,1.80,1.67,1.98]
#Para la posición
print(edades[-2])
print(edades[0:2])
print(edades[:3])
print(edades[2:])
print(edades[:])

#Para organizar
edades.sort()
print(edades)
edades.sort(reverse=True)
print(edades)
mayor = max(edades)
print(mayor)
menor = min(edades)
print(menor)

#Contar cuántos elementos hay
largoListaEdades = len (edades)
print(largoListaEdades)
sumaEdades = sum(edades)
print(sumaEdades)
#Promedio
PromedioEdades = sumaEdades/largoListaEdades
print(PromedioEdades)

#Eliminar un elemento
edades.pop(2)
print(edades)

##Ciclo for y litas
largoListaEdades = len (edades)
for indice in range (largoListaEdades):
    print(edades[indice])
LargoListaNombres = len (nombres)
for indice in range (LargoListaNombres):
    print(nombres[indice])

posicionesConValoresPares = []
largoListaEdades = len (edades)
for posicion in range (largoListaEdades):
    if (edades[posicion] % 2 == 0):
        posicionesConValoresPares.append(posicion)

print(edades)
print(posicionesConValoresPares)

#Solo cuando les interese mostrar la lista
for edad in edades:
    print(edad)
for nombre in nombres:
    print(nombre)
