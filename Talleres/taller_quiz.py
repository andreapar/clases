# ----- Entradas -----#
MensajeHola = "Hola, bienvenido"
PreguntaOpcion = ''' Ingrese alguna de estas opciones
    1. Hacer conversión de pesos a dolares o Euros
    2. Agrege un valor a la lista de pesos
    3. Mostrar valor más alto, más bajo y promedio
    4. Eliminar elemento de la lista
    5. Salir
:'''

PreguntaMoneda = ''' Ingrese alguna de estas opciones
    C. Mostar en pesos colombianos
    D. Mostar en Dolares
    E. Mostar en Euros
:'''

PreguntaNumero = "Ingrese un valor en COP: "
preguntaBorrarCoordenada = "Ingrese la posición que desea borrar:"
#----- Mensajes -----#
mensajePesos = "Mostrando lista original"
mensajeDolares = "Mostrar lista dolares"
mensajeEruros = "Mostar lista en euros"
mensajeError = "Valor ingresado no válido"
mensajeMayor = "El mayor número ingresado es: "
mensajeMenor = "El menor número ingresado es: "
mensajePromedio = "El promedio es: "

#-----Conversión punto 1 -----#
listaPesos = [2000,3000,4000,2500,1000,7600]
listaEuros = []
for elemento in listaPesos:
    convesor = round (elemento * 0.00023,2)
    listaEuros.append(convesor)

ListaDolares =[]
for elemento in listaPesos:
    convesor = round (elemento * 0.00028,2)
    ListaDolares.append(convesor)

#----- Código -----# 
print(MensajeHola)
opcionEscogida = int(input(PreguntaOpcion))
while(opcionEscogida != 5):
    # ------ Opción 1 ------ #
    if (opcionEscogida == 1):
        opcionMoneda = input(PreguntaMoneda)
        if (opcionMoneda == "C"):
            print(mensajePesos)
            print(listaPesos)
        elif (opcionMoneda == "D"):
            print(mensajeDolares)
            print(ListaDolares)
        elif (opcionMoneda == "E"):
            print(mensajeEruros)
            print(listaEuros)
        else:
            print(mensajeError)

    #----- Opción 2 -----#
    elif (opcionEscogida == 2):
        valorIngresado = float(input(PreguntaNumero))
        listaPesos.append(valorIngresado)
        print(listaPesos)

    #----- Opción 3 -----#
    elif (opcionEscogida == 3):
        print(mensajeMayor, max(listaPesos))
        print(mensajeMenor, min(listaPesos))
        print(mensajePromedio, sum(listaPesos)/ len(listaPesos))
    
    # ----- Opción 4 -----#
    elif (opcionEscogida == 4):
        print(listaPesos)
        posicion = int(input(preguntaBorrarCoordenada)) - 1
        listaPesos.pop(posicion)
        print(listaPesos)
    else:
        print(mensajeError)
    opcionEscogida = int(input(PreguntaNumero))

print("Feliz día")
