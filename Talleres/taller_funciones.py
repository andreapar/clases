import funcion as fn
preguntaOpcion = '''Ingrese alguna de estas opciones
    1. Mostrar lista de ciudades y materias
    2. Mostrar lista de números y los topes
    3. Mostrar los números mayores a 24 de la lista anterior
    4. Mostrar los números pares de la lista anterior
    5. Mostrar saludos
    6. Calcular el IMC
    7. Salir
'''
listaNumeros = [23,16,76,78,56,6,13,45,68,98,11,27,82,22,36,37]

#----- Código -----#
opcion = int(input(preguntaOpcion))
while (preguntaOpcion != 7):
    #----- Punto 1 -----#
    if (preguntaOpcion == 1):
        ciudades = ["Medellín", "Lisboa", "Ámsterdam", "Berlín","Cartagena", "Manizales"]
        materias = ["Geografía", "Historia", "Arte", "Música", "Química"]
        fn.mostrarLista(ciudades)
        fn.mostrarLista(materias)

    #----- Punto 2 -----#
    elif (preguntaOpcion == 2):
        fn.mostrarEstadistica(listaNumeros)

    #----- Punto 3 -----#
    elif (preguntaOpcion == 3):
        fn.listaPares(listaNumeros)

    #----- Punto 4 -----#
    elif(preguntaOpcion == 4):
        fn.listaMayor(listaNumeros)
        print("=================================")

    #----- Punto 5 -----#
    elif (preguntaOpcion == 5):
        fn.saludar

    #----- Punto 6 -----#
    elif (preguntaOpcion == 6):
        peso = float(input("Por favor ingresa tu peso en Kg: "))
        estatura = float(input("Por favor ingresa tu estatura en m:"))
        fn.calcularImc
        print("=================================")

    #----- Punto 7 -----#
    else:
        fn.despedida(Adios)
    opcion = int(input(preguntaOpcion))
