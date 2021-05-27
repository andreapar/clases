from os import system,name
import matplotlib.pyplot as plt
import sys

def limpiarPantalla():
    if (name == "nt"):
        _ = system("cls")
    else:
        _ = system("clear")

#----- Punto 1 -----#
listaAlimentos = []
listaValor = []
for i in range (8):
    alimento = input("Por favor ingrese su alimento favorito: ")
    valor = input("Ingrese el precio del alimento: ")
    listaValor.append (valor)
    listaAlimentos.append (alimento)
    print (f"Haga este proceso {7-i} veces")

print (listaAlimentos)
print (listaValor)

plt.bar (listaAlimentos,listaValor, width= 0.5, color = "m")
plt.title("Alimentos favoritos")
plt.xlabel("Alimentos")
plt.ylabel("Precio")
plt.savefig("Alimentosfav.png")
plt.show()

input("\nPresione una tecla para continuar.")

limpiarPantalla()

#----- Punto 2 -----#
class Humano ():
    '''Esta es la clase Humano, cuenta con atributos que lo hacen especial
        nombreEntrada: Hace referencia al nombre del usuario
        sexoEntrada: Hace referencia al sexo del usuario
        edadEntrada: Hace referencia a la edad del usuario

        Además, tiene dadas una serie de funciones que son:
            *hablar(mensaje):
                Recibe un mensaje y lo muestra en pantalla
            *mostrarAtributos():
                Muestra los atributos de la persona
    '''
    def __init__ (self,nombreEntrada,sexoEntrada,edadEntrada):
        self.nombre = nombreEntrada
        self.sexo = sexoEntrada
        self.edad = edadEntrada
    
    def hablar (self,mensaje):
        print(f"Hola soy {self.nombre} tengo un mensaje que decir...", mensaje)
    
    def mostrarAtributos (self):
        print(f'''Mi nombre es {self.nombre} y soy una {self.sexo} y mi edad es {self.edad} años''')

class Doctor (Humano):
    def calcularIMC (self,peso,estatura):
        imc = peso / (estatura**2)
        print(f"El IMC del paciente es: ",imc)

humano = Humano('Camil', 'mujer', '24')
humano.mostrarAtributos()
print ("\n")
humano.hablar("Hola, tengo mucho sueño porque me quedé viendo AOT")
print ("\n")
doctor1 = Doctor("Liz","femenino",29)
doctor1.calcularIMC(53,1.64)

input("\nPresione una tecla para continuar.")

limpiarPantalla()

#----- Punto 3 -----#
def ConversorEurosEnDolares ():
    isCorrectInfo = False
    while(isCorrectInfo == False):
        try:
            nombre = input("Ingrese su nombre: ")
            assert (nombre.isalpha())
            isCorrectInfo = True
        except AssertionError:
            print("Ingresaste un dato no válido")
    
    isCorrectInfo = False
    while(isCorrectInfo == False):
        try:
            dinero = float(input("Ingrese la cantidad de dinero en dólares: "))
            isCorrectInfo = True
        except ValueError:
            print("Ingresaste un dato no válido")

    print(f"Hola {nombre}, la cantidad de dinero que tienes en euros es {dinero*0.82}")
ConversorEurosEnDolares()

input("\nPresione una tecla para continuar.")

limpiarPantalla()

#----- Punto 4 -----#
nombreArchivo = "pacientes.txt"

try:
    archivo = open(nombreArchivo)
except FileNotFoundError:
    archivo = open(nombreArchivo, 'w', encoding="UTF-8")
    descripcionArchivo = "Clientes consultorio de neurología\n\n"
    archivo.writelines(descripcionArchivo)
    archivo.close()

nombrePaciente = input("Ingrese el nombre del paciente: ")
enfermedad = input("Ingrese la descripción de la enfermedad: ")
valorConsulta = 0

isCorrectInfo = False
while(isCorrectInfo == False):
    try:
        valorConsulta = int(input("Ingresa el valor de la consulta, por favor: "))
        isCorrectInfo = True
    except ValueError:
        print("Ingresaste un dato no válido")

archivo = open(nombreArchivo, 'a', encoding="UTF-8")
archivo.write(f"Paciente: {nombrePaciente}\n")
archivo.write(f"Descripción: {enfermedad}\n")
archivo.write(f"Precio mantenimiento: {valorConsulta}\n")
archivo.write("=========================\n")
archivo.close()

limpiarPantalla()

#----- Leer ---- #
print("El contenido del archivo de pacientes es:\n ")

with open(nombreArchivo, 'r') as reader:
    for line in reader:
        print(line)
