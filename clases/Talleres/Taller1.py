print("Hola, bienvenido a la calculadora")
opcion = 0
while(opcion != 5):
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. Divisón")
    print("5. Salir")
    opcion = int(input("Ingrese opcion\n"))
    if (opcion == 1 ):
        print("Selecciono Suma")
        a =float(input("Ingrese numero\n"))
        b =float(input("Ingrese numero\n"))
        resultado=a+b
        print("El resultado es: ",resultado)
        input()

    elif (opcion == 2 ):
        print("Selecciono Resta")
        a =float(input("Ingrese numero\n"))
        b =float(input("Ingrese numero\n"))
        resultado=a-b
        print("El resultado es: ",resultado)
        input()

    elif (opcion == 3 ):
        print("Selecciono Multiplicación")
        a =float(input("Ingrese numero\n"))
        b =float(input("Ingrese numero\n"))
        resultado=a*b
        print("El resultado es: ",resultado)
        input()

    elif (opcion == 4 ):
        print("Selecciono Divisón")
        a =float(input("Ingrese numero\n"))
        b =float(input("Ingrese numero\n"))
        if(b == 0 ) :
            print("No se puede dividir por 0")
        else:   
            resultado=a/b
            print("El resultado es: ",resultado)
        input()

print("Gracias, vuelva pronto")

