import conversorTemperaturas as ct
import funciones as fn
preguntaNumero = '''Ingrese alguna de estas opciones
    1. Convertir temperaturas
    2. Mostrar clasificación
    3. Mostar topes
    4. Salir
'''
preguntaTemperatura = '''
    K. Mostrar Kelvin
    F. Mostar Fahrenheint
    C. Mostrar Celsius
'''

#----- Mensajes -----#
mensajeCelsius = "Mostrando lista original"
mensajeKelvin = "Mostrar lista en kelvin"
mensajeFahrenheint = "Mostrar lista en fahrenheit"
mensajeDespedida = "Ten un lindo día"
mensajeError = "Valor ingresado no válido"

temperaturaCorporal = [36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33]

temperaturaFahrenheint = ct.conversionTemperatura(temperaturaCorporal,"F")
temperaturaKelvin = ct.conversionTemperatura(temperaturaCorporal, "K")
clasificacionTemperaturas = ct.clasificarTemperaturas(temperaturaCorporal)

opcionEscogida = int (input(preguntaNumero))
while (opcionEscogida !=4):
    #----- Opción 1 -----#
    if (opcionEscogida == 1):
        opcionConversion = input(preguntaTemperatura)
        if (opcionConversion == "C"):
            print("La conversión no era necesaria")
            print(mensajeCelsius)
        elif (opcionConversion == "F"):
            print(mensajeFahrenheint)
            fn.mostrarLista(temperaturaFahrenheint)
        elif (opcionConversion == "K"):
            print(mensajeKelvin)
            fn.mostrarLista(temperaturaKelvin)
        else:
            print(mensajeError)

    #----- Opción 2 -----#
    elif (opcionEscogida == 2):
        print("Mostrando clasificación")
        print("°C", "\t", "Clasificación")
        fn.mostrar2Lista(temperaturaCorporal,clasificacionTemperaturas)

    #----- Opción 3 -----#
    elif (opcionEscogida == 3):
        ct.mostrarTopes(temperaturaCorporal)
    
    #----- Opción no válida ----- #
    else:
        print(mensajeError)
    opcionEscogida = int(input(preguntaNumero))
print(mensajeDespedida)
