#----- Punto 1 -----#
class Persona ():
    '''Esta es la clase Persona, cuenta con atributos que lo hacen especial
        nombreEntrada: Hace referencia al nombre del usuario
        idEntrada: Hace referencia a la identificación del usuario
        edadEntrada: Hace referencia a la edad del usuario

        Además, tiene dadas una serie de funciones que son:
            *hablar(mensaje):
                Recibe un mensaje y lo muestra en pantalla
            *caminar(acción):
                Describe cuánto pasos a dado en el día
            *mostrarAtributos():
                Muestra los atributos del porqué lo hace Persona
    '''
    def __init__ (self,nombreEntrada,idEntrada,edadEntrada):
        self.nombre = nombreEntrada
        self.id = idEntrada
        self.edad = edadEntrada
    
    def hablar (self,mensaje):
        print(f"Hola soy {self.nombre} tengo un mensaje que decir...", mensaje)
    
    def caminar (self, pasos):
        print (f"{self.nombre} ha dado {pasos} pasos mientras caminaba en el parque")
    
    def mostrarAtributos (self):
        print(f'''Mi nombre es {self.nombre} mi identificación es {self.id} y mi edad es {self.edad} años''')

#-----Punto 2 -----#

class Doctor(Persona):
    def __init__ (self,nombreEntrada,idEntrada,edadEntrada,especialidadEntrada):
        Persona.__init__(self,nombreEntrada,idEntrada,edadEntrada)
        self.especialidad = especialidadEntrada

    def tratamiento (self,enfermedad):
        print (f"Hola soy {self.nombre} soy especialista en {self.especialidad} y te ayudaré a tratar tu {enfermedad}")
    
    def mostrarAtributos (self):
        super().mostrarAtributos()
        print(f"Mi especialidad es {self.especialidad}")

#-----Punto 3 -----#

class Nutricionista(Persona):
    def __init__ (self,nombreEntrada,idEntrada,edadEntrada,universidadEntrada):
        Persona.__init__(self,nombreEntrada,idEntrada,edadEntrada)
        self.universidad = universidadEntrada

    def calcularImc (self,pesoEntrada,alturaEntrada):
        imc = pesoEntrada/(alturaEntrada**2)
        print(f"Hola soy {self.nombre} y mi IMC calculado es {imc}")
    
    def mostrarAtributos (self):
        super().mostrarAtributos()
        print(f"Mi universidad es {self.universidad}")

#----- Punto 4 -----#

class Abogado (Persona):
    def __init__ (self,nombreEntrada,idEntrada,edadEntrada,universidadEntrada,especialidadEntrada):
        Persona.__init__(self,nombreEntrada,idEntrada,edadEntrada)
        self.universidad = universidadEntrada
        self.especialidad = especialidadEntrada
    
    def representarCaso (self,caso):
        print(f"El/La abogad@ procede a representar al cliente {self.nombre} en el caso {caso}")
    
    def mostrarAtributos (self):
        super().mostrarAtributos()
        print(f"Mi universidad es {self.universidad} y mi especialidad es {self.especialidad}")

persona1 = Persona("Elena",1001465854,25)
persona2 = Persona("Camil",1004557911,19)
print("========================================================================")

persona1.hablar("Tengo ganas de un helado")
persona2.caminar(12)
print ("\n")
persona1.mostrarAtributos()
print("========================================================================")

doctor1 = Doctor("Ashs",100146798,25,"Pediatría")
doctor2 = Doctor("Jules",10176991,31,"Neurología")
doctor1.tratamiento("Anemia")
print ("\n")
doctor2.mostrarAtributos()
print("========================================================================")

nutricionista1 = Nutricionista("Becca",10015787,26,"CES")
nutricionista1.mostrarAtributos()
print ("\n")
nutricionista1.calcularImc(45,1.68)
print("========================================================================")

abogado1 = Abogado("Eiji",100141716,28,"UMedellín","Tributario")
abogado1.representarCaso("Manejo de dinero en la empresa D")
print ("\n")
abogado1.mostrarAtributos()

