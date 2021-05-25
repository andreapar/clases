from os import system,name
import sys

def limpiarPantalla():
    if (name == "nt"):
        _ = system("cls")
    else:
        _ = system("clear")

#------ Punto 1 -----#
saludo = "Hola, espero que este bien"
preguntaEstatura = "Por favor ingrese su estatura: "
preguntaPeso = "Por favor ingrese su peso: "
resultadoImc = "Tu IMC calculado es:"
peso = 0
estatura = 0

print(saludo)
isCorrectInfo = False
while(isCorrectInfo == False):
    try:
        nombre = input("Ingrese su nombre: ")
        assert(nombre.isalpha())
        isCorrectInfo = True
    except AssertionError:
        print("Ingresaste un dato no valido")

isCorrectInfo = False
while(isCorrectInfo == False):
    try:
        peso = float(input(preguntaPeso))

        if peso > 0:
            isCorrectInfo = True
        else:
            print("El peso debe ser mayor a cero.")
    except ValueError:
        print("Ingresaste un dato no válido")

isCorrectInfo = False
while(isCorrectInfo == False):
    try:
        estatura = float(input(preguntaEstatura))

        if estatura > 0:
            isCorrectInfo = True
        else:
            print("La estatura debe ser mayor a cero.")
    except ValueError:
        print("Ingresaste un dato no válido")

IMC = peso / (estatura ** 2)
print(f"El IMC es: {round(IMC, 2)}")

input("\nPresione una tecla para continuar.")
    
limpiarPantalla()

#----- Punto 2 -----#
preguntaParrafo =" Por favor ingrese un párrafo: "
isCorrectInfo = False
parrafo = ""

while(isCorrectInfo == False):
    parrafo = input(preguntaParrafo)
    isCorrectInfo = parrafo.endswith('.')

    if (isCorrectInfo == False):
        print("El párrafo debe termninar con punto")

palabras = parrafo.split()
palabraMayor = max(palabras,key=len)
palabraMenor = min(palabras,key=len)

print(f"La palabra mayor es: {palabraMayor}")
print(f"La palabra menor es: {palabraMenor}")

input("\nPresione una tecla para continuar.")
    
limpiarPantalla()

#----- Punto 3 ----- #
nombreArchivo = "mantenimiento.txt"

try:
    archivo = open(nombreArchivo)
except FileNotFoundError:
    archivo = open(nombreArchivo, 'w', encoding="UTF-8")
    descripcion = "Archivo para manejo de clientes\n\n"
    archivo.writelines(descripcion)
    archivo.close()

equipoMedico = input("Ingrese el nombre del equipo médico: ")
descripcion = input("Ingrese la descripción: ")
valorMantenimiento = 0

isCorrectInfo = False
while(isCorrectInfo == False):
    try:
        valorMantenimiento = int(input("Ingresa el precio del mantenimiento: "))
        isCorrectInfo = True
    except ValueError:
        print("Ingresaste un dato no válido")

archivo = open(nombreArchivo, 'a', encoding="UTF-8")
archivo.write(f"Equipo: {equipoMedico}\n")
archivo.write(f"Descripción: {descripcion}\n")
archivo.write(f"Precio mantenimiento: {valorMantenimiento}\n")
archivo.write("======================\n")
archivo.close()

limpiarPantalla()

#----- Leer ---- #
print("El contenido del archivo de mantenimiento es:\n ")

with open(nombreArchivo, 'r') as reader:
    for line in reader:
        print(line)
