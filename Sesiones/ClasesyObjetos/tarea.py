class Zorro:
    '''Esta es la clase Zorro, una criatura insual y amigable,
    tiene varios atributos que los diferencian entre ellos:
    nombreEntrada: Hace referencia al tipo de Zorro
    pelajeEntrada: Hace referencia al color de su pelaje
    generoEntrada: Hace referencia a si es macho o hembra
    habitatEntrada: Hace referencia al hábitat donde esta
    Además, tiene las siguientes acciones:
    *jugar(accion):
        Describe cómo es feliz
    *cazar(accion):
        Describe cual es su alimentación  favorita
    *mostrarAtributos():
        Muestra los atributos del porqué lo hace especial
    '''

    def __init__(self,nombreEntrada,pelajeEntrada,generoEntrada,habitatEntrada):
        print("Hola, soy un zorro astuto")
        self.nombre = nombreEntrada
        self.pelaje = pelajeEntrada
        self.genero = generoEntrada
        self.habitat = habitatEntrada

    def jugar (self):
        print(f"Hola soy {self.nombre}  y me divierto mucho jugando en la nieve")

    def mostrarAtributos (self):
        print(f'''Soy el zorro {self.nombre} y soy una/o {self.genero}.
                Tengo el pelaje del color {self.pelaje} lo que me diferencia
                de los demás y habito normalmente en {self.habitat}
        ''')

    def cazar (self):
        print(f"Soy el zorro {self.nombre} y mi alimentación es de bayas y frutos")

zorro1 = Zorro("vulpes vulpe", "rojo", "macho", "Hemisferio norte")
zorro2 = Zorro("Vulpes lagopus", "blanco", "hembra", "Eurasia y Norteamérica")
zorro3 = Zorro("Vulpes zerda","arena", "macho", "Desirto delSáhara")

zorro1.mostrarAtributos()
print("================================")
zorro2.jugar()
zorro2.mostrarAtributos()
print("================================")
zorro3.cazar()

