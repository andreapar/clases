# Intregrantes: Santiago Díaz, Ángel Muñoz y Andrea Parra #

#----- Punto 1 ------#
class ElementoDigital ():
    '''Esta clase ElemntoDigital cuenta con varios atrubutos que la hacen única
    uno de ellos es nombre, creador y fecha de publicación'''

    def __init__ (self,nombreEntrada, creadorEntrada, fechaEntrada):
        self.nombre = nombreEntrada
        self.creador = creadorEntrada
        self.fecha = fechaEntrada

    def mostrarAtributos (self):
        print(f'''La aplicación es {self.nombre}, el creador del elemento digital es {self.creador}, 
        un gran programador para su siglo que creó está aplicación el día {self.fecha} para ser la mejor ''')

elemento1 = ElementoDigital("In Academia", "Camil Ackerman", "25/06/2021")
elemento1.mostrarAtributos()
print("========================================================================")

class Pagina ():
    '''En la clase Pagina puedes encontrar diversos atributos que la hacen única y una de las mejores páginas de la web'''

    def __init__(self, tipodecontenidoh, formatoh, fechah):
        self.tipo = tipodecontenidoh
        self.formato = formatoh
        self.fecha = fechah

    def mostrarAtr(self):
        print(f'''En mi página hay contenido sobre {self.tipo}, en un formato {self.formato}
        y se público en el {self.fecha}''')

pag = Pagina ("Música", "PHP", 2012)
pag.mostrarAtr()
print("========================================================================")

class Usuario ():
    '''Esta en la clase Usuario, cuenta con atributos que lo ayudan a diferenciar de otros usuiarios,
    estos son: nombre, edad, sexo y nacionalidad'''

    def __init__ (self,nombreEntrada,edadEntrada, sexoEntrada, nacionalidadEntrada):
        self.nombre = nombreEntrada
        self.edad = edadEntrada
        self.sexo = sexoEntrada
        self.nacionalidad = nacionalidadEntrada
    
    def mostrarA (self):
        print(f'''Hola soy {self.nombre}, tengo {self.edad} años ,
        mi sexo es {self.sexo} y soy de {self.nacionalidad}''')

usuario = Usuario ("Duvan",30,"masculino","Colombia")
usuario.mostrarA()
print("========================================================================")

#----- Punto 2 ----#
class Cancion (ElementoDigital):
    def __init__ (self,nombreEntrada, creadorEntrada, fechaEntrada,generoMusicalEntrada,duracionEntrada):
        ElementoDigital.__init__ (self,nombreEntrada, creadorEntrada, fechaEntrada)
        self.generoMusical = generoMusicalEntrada
        self.duracion = duracionEntrada
    
    def mostrarCancion (self):
        print(f'''La canción es History es de género {self.generoMusical} y es de la banda musical 1D, 
        dura apox {self.duracion} minutos y es de las mejores canciones del siglo''')
    
    def reproducir (self,cancion):
        for i in range (cancion):
            print(f" La canción es {self.nombre} y ha sonado {i + 1} veces")

cancion = Cancion("History","1D","26/01/2016","Pop", 3.15)
cancion.mostrarCancion()
print("========================================================================")
cancion.reproducir(6)
print("========================================================================")

class Artista (Usuario):
    def __init__ (self,nombreEntrada,edadEntrada, sexoEntrada, nacionalidadEntrada,generoEntrada,cancionesPublicadasIn,albumEntrada):
        Usuario.__init__ (self,nombreEntrada,edadEntrada, sexoEntrada, nacionalidadEntrada)
        self.genero = generoEntrada
        self.canciones = cancionesPublicadasIn
        self.album = albumEntrada

    def concierto (self,ciudad):
        print(f"Hola soy {self.nombre} un artista reciente y daré un concierto en la noche en  {ciudad}")

angel = Artista("Ángel",19,"masuculino","colombiano","Pop alternativo",30,7)
angel.concierto("Medellín")
print("========================================================================")

class Favoritos(Pagina):
    def __init__(self,tipodecontenidoh, formatoh, fechah,favcomui,fechaActualizacion):
        Pagina.__init__ (self,tipodecontenidoh, formatoh, fechah)
        self.favoritocomunidad = favcomui
        self.fechaActualizacion = fechaActualizacion

    def agrgarSong (self, cancion, actualizacion):
        self.favoritocomunidad.append(cancion)
        self.fechaActualizacion = actualizacion

    def mostrarLista (self, cancionEliminida):
        print(self.favoritocomunidad)
        self.favoritocomunidad.pop(cancionEliminida)

lista = ["History", "End of the day", "Infinity", "Angel", "Drag me down", "One thing"]
oneDirection = Favoritos ("Cancion", "mp3", 2020, lista, 2021)
oneDirection.mostrarLista(3)
print("========================================================================")
oneDirection.agrgarSong("Best song ever",2021)
print(oneDirection.favoritocomunidad)
