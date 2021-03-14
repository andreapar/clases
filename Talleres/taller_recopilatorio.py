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
    print("")
    if (opcion == 1):
        conversion = input(PreguntarConversion)
        if (conversion == "C"):
            print(MensajePesos)
            print(listaPesos)
        elif (conversion == "D"):
            print(MensajeDolares)
            print(listaDolares)
        elif (conversion == "E"):
            print(MensajeEruros)
            print(listaEuros)
        else:
            print(MensajeNoValido)
        print "=" * 30
    elif (opcion == 2)
    







