class Humano ():
    '''
        Esta es la clase Humano exige atributos
        nombreEntrada: Hace referencia al nombre del usuario
        edadEntrada: Hace referencia al edad del usuario
        estaturaEntrada: Hace referencia al estatura del usuario
        
        Tiene las siguientes acciones:

        *hablar(mensaje):
            dado un mensaje lo muestra en pantalla
        
        *mostrarAtributos()
            muestra los atributos del usuario
    '''
    def __init__(self,nombreEntrada,edadEntrada):
        print("Hola, soy un humano nuevo")
        self.edad = edadEntrada
        self.raza = "Humano"
        self.nombre = nombreEntrada
        self.estatura = edadEntrada
        self.dinero = 0

    
    def hablar(self,mensaje):
        print("Hola soy {self.nombre} tengo un mensaje que decir...", mensaje)
    
    def mostrarAtributos (self):
        print(f'''Mi nombre es {self.nombre}
                    Mi estatura es {self.altura} metros
                    Mi edad es {self.edad} años
                    Tengo ahorrado {self,dinero}pesos
        ''')

    def recorrerDistancia(self,distanciaMetros):
        for i in range (distanciaMetros):
            print(f"Hola soy {self.nombre} y he recorrido {i + 1} metros")

    def ahorraDinero(self):
        preguntaIngresarMonto = "Ingrese S para continuar añadiendo montos y N para finalizar"
        preguntaMonto = "¿Cuánto vas a ingresar?: "
        ingresarMontos = input(preguntaIngresarMonto)
        while(ingresarMontos != "N"):
            monto = 


humano1 = Humano("Armin",19,1.60)
humano2 = Humano("Kousei",20,1.67)

humano1.hablar("Esta haciendo un día lindo")
humano2.hablar("Adiós amigo")
print(humano1.nombre)
print(humano2.nombre)
print(humano2.altura)
humano1.mostrarAtributos()
humano2.mostrarAtributos()
humano1.recorrerDistancia(25)
totalAhorrado = humano2.ahorrarDinero()
print(totalAhorrado)
