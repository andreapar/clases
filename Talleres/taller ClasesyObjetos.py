#----- Punto 1 -----#
class Torta ():
    ''' Esta clase Torta contiene algunos atributos que son:
        formaEntrada: Hace referencia a la forma de la torta
        saborEntrada: Hace referencia al sabor de la torta
        alturaEntrada: Hace referencia a la altura de la torta
    '''

    def __init__ (self,formaEntrada, saborEntrada,alturaEntrada):
        self.forma = formaEntrada
        self.sabor = saborEntrada
        self.altura = alturaEntrada
    
    def mostrarAtributos (self):
        print(f"Hola,la torta que pediste es de forma {self.forma}, sabor {self.sabor} y de {self.altura} cm de altura")

torta1 = Torta ("Redonda","milo",8)
torta1.mostrarAtributos()
print("========================================================================")

#----- Punto 2 -----#
class Estudiante ():
    '''La clase Estudiante tiene diversos atributos que hacen único al estudiante
        de cada clase, estos son: Nombre,edad, ID, carrera y semestre'''
    
    def __init__ (self,nombreEntrada,idEntrada,carreraEntrada,semestreEntrada, edadEntrada):
        self.nombre = nombreEntrada
        self.edad = edadEntrada 
        self.id = idEntrada
        self.carrera = carreraEntrada
        self.semestre = semestreEntrada
    
    def mostrarAtributos (self):
        print(f''' Mi nombre es {self.nombre} y tengo {self.edad}, mi ID es {self.id}. 
    Estoy estudiando {self.carrera} y voy en el semestre {self.semestre}''')
    
    def estudiarMateria  (self, materiaEntrada, horasEntrada):
        self.materia = materiaEntrada
        self.horas = horasEntrada
        print(f"Soy {self.nombre} y voy a estudiar {self.materia} por {self.horas} horas")

estudiante1 = Estudiante("Violet",1007898056,"Arquitectura",6,18)
estudiante1.mostrarAtributos()
estudiante1.estudiarMateria("Taller",5)
print ("\n")
estudiante2 = Estudiante("Erica",100987152,"Medicina",3,17)
estudiante2.estudiarMateria("Salud Pública",6)
print("========================================================================")

#----- Punto 3-----#
class Nutricionista ():
    '''Esta es la clase Nutricionista, donde se muuestra los datos del profesional.
        Además, te ayuda a calcular tu índice de masa corporal(IMC).'''

    def __init__ (self, nombreEntrada, edadEntrada, universidadEntrada):
        self.nombre = nombreEntrada
        self.edad = edadEntrada
        self.universidad = universidadEntrada
    
    def mostrarAtributos (self):
        print(f"Mi universidad es {self.universidad}")
    
    def calcularImc (self,pesoEntrada,alturaEntrada):
        imc = pesoEntrada/(alturaEntrada**2)
        print(f"Hola soy {self.nombre} y mi IMC calculado es {imc}")
    
nutricionista = Nutricionista("Ariel",27,"CES")
nutricionista.calcularImc(43,1.65)
nutricionista.mostrarAtributos()
print("========================================================================")

#----- Punto 4 -----#
class Canguro ():
    '''En la clase Canguro, encontrarás el nombre,la edad y el ID. 
    También, muestra la cantidad de saltos que ha dado.
    '''

    def __init__ (self,nombreEntrada,edadEntrada,idEntrada):
        self.nombre = nombreEntrada
        self.edad = edadEntrada
        self.id = idEntrada
    
    def saltar (self, cantidadSaltos):
        for i in range (cantidadSaltos):
            print(f"Hola mi nombre es {self.nombre}, soy un canguro y hoy he dadoo {i+1} saltos")

canguro = Canguro("Aslan",2,541)
canguro.saltar(7)
print("========================================================================")

#----- Punto 5 -----#
class Piano ():
    '''Esta es la clase Piano, donde con solo el arte de las teclas
    puedes transmitir lo que sientes y llegar al público.'''

    def __init__ (self, tipoEntrada,marcaEntrada,añosEntrada):
        self.tipo = tipoEntrada
        self.marca = marcaEntrada
        self.años = añosEntrada
    
    def tocarPiano (self,cancion):
        print (f"Andrea está tocando la cancion {cancion} en el piano {self.tipo} que tiene {self.años} años de uso")

piano1 = Piano("Piano digital","Casio",1)
piano1.tocarPiano("Faded")
print ("\n")
piano2 = Piano("Piano de cola","Yamaha",4)
piano2.tocarPiano("Love's Sorrow")
