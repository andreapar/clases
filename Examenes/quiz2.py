from os import system,name

MensajeBienvenido = "Hola, hoy te ayudaremos con tus temperaturas"
PreguntaMenu = ''' Menú de opciones
    1. Conversión de temperatura
    2. Conocer estado del paciente
    3. Conocer el máximo, mínimo y toma de datos
    4. Salir del programa
Ingresa la opción seleccionada: '''

PreguntaConvertir = '''
    F. Para mostrar en Fahrenheit
    K. Para mostrar en Kelvin
    C. Para mostrar en Celsius
Ingrese la opción seleccionada: '''

#---- Mensajes -----#
MensajeFahrenheit = "Mostar lista en Fahrenheit"
MensajeKelvin = "Mostar lista en Kelvin"
MensajeCelsius = "La conversión no es necesaria"
MensajeHipotermia = "Cuidado, el paciente tiene hipotermia"
MensajeFiebre = "El paciente tiene fiebre"
MensajeTemperaturaNormal = "Está en estado normal de temperatura"
MensajeMaxima = "Su temperatura máxima fue:"
MensajeMinima = "Su temperatura minima fue:"
MensajeError = "Entrada no válida"
MensajeAdios = "Gracias, vuelva pronto"

listaCelsius = [36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33]
listaFahrenheit = []
for elemento in listaCelsius:
    conversor = round((elemento * 1.8) + 32)
    listaFahrenheit.append(conversor)

listaKelvin = []
for elemento in listaCelsius:
    convesor = round(elemento + 273.15)
    listaKelvin.append(convesor)

#---- Código ----#
print(MensajeBienvenido)
opcion = int(input(PreguntaMenu))
while(opcion != 4):
    #----- Opción 1 ----#
    if (opcion == 1):
        temperaturas = input(PreguntaConvertir)
        if (temperaturas.upper() == "C"):
            print(MensajeCelsius)
            print(listaCelsius)
        elif (temperaturas.upper() == "F"):
            print(MensajeFahrenheit)
            print(listaFahrenheit)
        elif (temperaturas.upper() == "K"):
            print(MensajeKelvin)
            print(listaKelvin)
        else:
            print(MensajeError)
    #----- Opción 2 -----#
    elif (opcion == 2):
        for elemento in listaCelsius:
            if (elemento < 36):
                print("-", elemento, "----->", MensajeHipotermia)
            elif (elemento >= 37.6):
                print("-", elemento, "----->", MensajeFiebre)
            elif (elemento >= 36 and elemento < 37,5):
                print("-", elemento, "----->", MensajeTemperaturaNormal)
    #----- Opción 3 -----#
    elif (opcion == 3):
        print(MensajeMaxima, max(listaCelsius))
        print(MensajeMinima, min(listaCelsius))
        print("La temperatura se tomaba cada", round(24/ len(listaCelsius),2), "horas")
    
    else:
        print(MensajeError)
    
    input("\nPresione una tecla para continuar.")
    
    if (name == "nt"):
        _ = system("cls")
    else:
        _ = system("clear")

    opcion = int(input(PreguntaMenu))

print(MensajeAdios)
