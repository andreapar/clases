isCorreInfo = False
while (isCorreInfo == False):
    try:
        edad = int(input("Ingrese su edad: "))
        isCorreInfo = True
    except ValueError:
        print("Ingresaste un dato no válido")

nombreArchivo = input("Ingrese el nombre del archivo que desea encontrar: ")
try:
    archivo = open (nombreArchivo)
except FileNotFoundError:
    print(f"El archivo {nombreArchivo} no se ha encontrado")

base = 4
divisor = 0
try:
    divir = base/divisor
except ZeroDivisionError:
    print("El divisor ingresado es igual a 0 por lo tanto es imposible dividir")

nombre = "Armin"
print(nombre.isalpha())
assert (nombre.isalpha())

isCorreInfo = False
while (isCorreInfo == False):
    try:
        nombre = input("Ingrese su nombre: ")
        assert (nombre.isalpha())
        isCorreInfo = True
    except AssertionError:
        print("Ingresaste un dato no válido")

isCorreInfo = False
while (isCorreInfo == False):
    try:
        edad = int(input("Ingrese su edad: "))
        assert (edad >= 18)
        isCorreInfo = True
    except AssertionError:
        print("Los menores de edad no pueden acceder")
    except ValueError:
        print("Las edades son números enteros")

lista = [2,18,25,2]
try:
    lista[5]
except IndexError:
    print("El indíce es mayor al tamaño de la lista")
