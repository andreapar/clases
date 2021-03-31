import funcion as fn

preguntaOpcion = '''Ingrese alguna de estas opciones
    1. Mostrar lista de ciudades y materias
    2. Mostrar lista de números y los topes
    3. Mostrar saludos 
    4. Mostrar los números pares de la lista anterior
    5. Mostrar los números mayores a 24 de la lista anterior
    6. Calcular el IMC
    7. Salir
'''

listaNumeros = [23,16,76,78,56,6,13,45,68,98,11,27,82,22,36,37]

#----- Código -----#
fn.limpiarPantalla ()

print("Hola, bienvenido")
opcion = int(input(preguntaOpcion))
while (preguntaOpcion != 7):
    fn.limpiarPantalla()

    #----- Punto 1 -----#
    if (opcion == 1):
        ciudades = ["Medellín", "Lisboa", "Ámsterdam", "Berlín","Cartagena", "Manizales"]
        materias = ["Geografía", "Historia", "Arte", "Música", "Química"]

        fn.mostrarLista(ciudades)
        print("================================")
        fn.mostrarLista(materias)

    #----- Punto 2 -----#
    elif (opcion == 2):
        mayor = fn.mayor(listaNumeros)
        menor = fn.menor(listaNumeros)
        promedio = fn.promedio(listaNumeros)

        print("El número más grande es:", mayor)
        print("El número menor es:", menor)
        print("El promedio es:", promedio)

    #----- Punto 3 -----#
    elif (opcion == 3):
        cantidad = int(input("Por favor ingresa la cantidad de saludos: "))
        fn.saludar(cantidad)

    #----- Punto 4 -----#
    elif(opcion == 4):
        pares = fn.listaPares(listaNumeros)
        fn.mostrarLista(pares)
        
    #----- Punto 5 -----#
    elif (opcion == 5):
        numerosMayores = fn.listaMayor(listaNumeros,24)
        fn.mostrarLista(numerosMayores)

    #----- Punto 6 -----#
    elif (opcion == 6):
        peso = float(input("Por favor ingresa tu peso en Kg: "))
        estatura = float(input("Por favor ingresa tu estatura en m: "))
        imc = fn.calcularImc(peso,estatura)
        print("El IMC es: ", imc)

    #----- Punto 7 -----#
    else:
        fn.despedida()

    fn.pausa()

    fn.limpiarPantalla

    opcion = int(input(preguntaOpcion))
