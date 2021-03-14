MensajeBienvenida = "Hola, hoy te ayudaremos cons tus negocios"
PreguntarOpcion = ''' Menú de opciones
    1. Conventir en dólares
    2. Clasificación de sus ingresos
    3. Conocer el máximo, mínimo y el promedio de sus ingresos
    4.Salir
Ingrese la opción seleccionada: '''

PreguntarConversion = '''
    C. Mostrar la lista en pesos colombianos
    D. Mostrar la lista en dólares
    E. Mostrar en euros
Ingrese una opción: '''

#---- Mensajes----
MensajePesos = "Mostrar lista en pesos"
MensajeDolares = "Mostrar lista original"
MensajeEruros = "Mostar lista en euros"
MensajeNoValido = "Entrada no válida"
MensajeIngresoBajo = "Ingresos bajos"
MensajeIngresoMedio = "Ingresos medios"
MensajeIngresoAlto = "Ingresos altos"
MensajeIngresoElevado = "Ingresos elevados"
MensajeMaximo = "Su ingreso más alto es"
MensajeMinimo = "Su ingreso más bajo es"
MensajePromedio = "Su promedio de los ingresos es"

listaDolares = [20000,30000,4000,2500,1000,7600]
listaPesos = []
for elemento in listaDolares:
    pesos = round (elemento * 3700,2)
    listaPesos.append (pesos)

listaEuros = []
for elemento in listaDolares:
    pesos = round (elemento * 0.84,2)
    listaEuros.append (pesos)

#----- Código -----#
print(MensajeBienvenida)
opcion = int(input(PreguntarOpcion))
while(opcion != 4):
    #-----Opción 1 -----#
    if (opcion == 1):
        conversion = input(PreguntarConversion)
        if (conversion.upper() == "C"):
            print(MensajePesos)
            print(listaPesos)
        elif (conversion.upper() == "D"):
            print(MensajeDolares)
            print(listaDolares)
        elif (conversion.upper() == "E"):
            print(MensajeEruros)
            print(listaEuros)
        else:
            print(MensajeNoValido)
    #----- Opción 2 -----#
    elif (opcion == 2):
        for elemento in listaDolares:
            if (elemento < 1000):
                print(elemento, MensajeIngresoBajo)
            elif (elemento >= 100 and elemento < 7000):
                print(elemento,MensajeIngresoMedio)
            elif (elemento >= 700 and elemento < 2000):
                print(elemento, MensajeIngresoAlto)
            else:
                print(elemento, MensajeIngresoElevado)
    #---- Opción 3 -----#
    elif (opcion == 3):
        print(MensajeMaximo, max (listaDolares))
        print(MensajeMinimo, min (listaDolares))
        print(MensajePromedio,sum (listaDolares)/len(listaDolares))
        print("===================================")
    else:
        print(MensajeNoValido)
    opcion = int(input(PreguntarOpcion))
print("Gracias, hasta pronto")


        