texto = "Hola, espero que estes bien"
lista = [2,4,6,8,10,12]
lista.sort ()

for elemento in lista:
    print(elemento)
for i in range (len(lista)):
    print(lista[i])

for letra in texto:
    print(letra)
print ("\n")
print(texto[1])
palabras = texto.split(" ")
print(palabras) 
eliminarE = texto.split("e")
print(eliminarE)

datos = "nombre;apellido;edad"
print(datos.split(";"))
print(datos)

#El join es para unir todos los elementos de la lista
uniendo = "i".join(eliminarE)
print(uniendo)
info =" ".join(datos.split(";"))
print(info)

#Comparación
listaNombres = ["Laura", "Juan", "Mario","Elsa","Katherine","daniel","Raul"]
print(max(listaNombres))
print(max(listaNombres, key=len))

respuesta = input("Ingrese Si o No: ")
print(respuesta.upper())
if respuesta.upper() == "SI":
    print("Hola bienvenidos al código")
else:
    print("Chao")

nombre = input("Ingrese su nombre: ")
print(nombre.capitalize())

correo = "ESPERO QUE ESTES BIEN"
print(correo.casefold().capitalize())
saludo = "Hola, ¿cómo estás?"
nombre = "Maria Sofia"
nombre = "maria sofia"
nombres = nombre.split(" ")
nombre = " "
for elemento in nombres:
    nombre += elemento.capitalize() +" "
print(nombre)
print(saludo.center(50))
print(nombre.center(50))

enunciado = "hola hola ya me cansé de decir tantos Hola"
print(enunciado.upper().count("HOLA"))

print(enunciado.find("decir"))
print(enunciado[25:30])

txt = "me gusta el helado de chocolate"
print(txt.replace("chocolate", "vainilla"))

numeroId = "123124"
print(numeroId.isnumeric())

parrafo = "If you think reality is just living comfortably and following your own whims, can you seriously dare to call yourself a soldier"
print(parrafo.endswith("."))



