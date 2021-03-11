from os import system, name

# ----- Entradas -----#
MensajeHola = "Hola, bienvenido"
PreguntaOpcion = ''' Menú de opciones
    1. Hacer conversión de pesos a dolares o euros
    2. Agrege un valor a la lista de pesos
    3. Mostrar valor más alto, más bajo y promedio
    4. Eliminar elemento de la lista
    5. Salir
Ingrese la opción seleccionada: '''

PreguntaMoneda = ''' Menú de conversiones
    C. Mostrar en pesos colombianos
    D. Mostar en dolares
    E. Mostrar en euros
Ingrese la opción seleccionada: '''

PreguntaNumero = "Ingrese un valor en COP: "
PreguntaBorrarCoordenada = "Ingrese la posición que desea borrar: "
#----- Mensajes -----#
MensajePesos = "Mostrando lista original"
MensajeDolares = "Mostrar lista dolares"
MensajeEruros = "Mostrar lista en euros"
MensajeError = "Valor ingresado no válido"
MensajeMayor = "El mayor número ingresado es: "
MensajeMenor = "El menor número ingresado es: "
MensajePromedio = "El promedio es: "

#-----Conversión punto 1 -----#
listaPesos = [2000,3000,4000,2500,1000,7600]
ListaEuros = []
for elemento in listaPesos:
    convesor = round (elemento * 0.00023,2)
    ListaEuros.append(convesor)

ListaDolares =[]
for elemento in listaPesos:
    convesor = round (elemento * 0.00028,2)
    ListaDolares.append(convesor)

#----- Código -----# 
print(MensajeHola)
OpcionEscogida = int(input(PreguntaOpcion))
while(OpcionEscogida != 5):
    print("")
    # ------ Opción 1 ------ #
    if (OpcionEscogida == 1):
        opcionMoneda = input(PreguntaMoneda)
        if (opcionMoneda.upper() == "C"):
            print(MensajePesos)
            print(listaPesos)
        elif (opcionMoneda.upper() == "D"):
            print(MensajeDolares)
            print(ListaDolares)
        elif (opcionMoneda.upper() == "E"):
            print(MensajeEruros)
            print(ListaEuros)
        else:
            print(MensajeError)

    #----- Opción 2 -----#
    elif (OpcionEscogida == 2):
        valorIngresado = float(input(PreguntaNumero))
        listaPesos.append(valorIngresado)
        print(listaPesos)

    #----- Opción 3 -----#
    elif (OpcionEscogida == 3):
        print(MensajeMayor, max(listaPesos))
        print(MensajeMenor, min(listaPesos))
        print(MensajePromedio, sum(listaPesos)/ len(listaPesos))

    # ----- Opción 4 -----#
    elif (OpcionEscogida == 4):
        print(listaPesos)
        posicion = int(input(PreguntaBorrarCoordenada)) - 1
        if (len(listaPesos) >= posicion):
            listaPesos.pop(posicion)
            print(listaPesos)
    else:
        print(MensajeError)

    input("\nPresione una tecla para continuar.")

    if (name == "nt"):
        _ = system("cls")
    else:
        _ = system("clear")

    OpcionEscogida = int(input(PreguntaOpcion))

print("Feliz día")
