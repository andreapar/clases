from os import system, name
# Limpiar consola en Python:https://www.geeksforgeeks.org/clear-screen-python/

opcion = 0

while(opcion != 6):
    if (name == "nt"):
        _ = system("cls")
    else:
        _ = system("clear")

    print("==================================================")
    print("Bievenidos a tu sistema de operaciones aritméticas")
    print("==================================================\n")

    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Mayor, menor o igual")
    print("6. Salir\n")
    opcion = int(input("Ingrese opción: "))

    if (name == "nt"):
        _ = system("cls")
    else:
        _ = system("clear")

    if (opcion == 1):
        print("===============")
        print("Operación Suma")
        print("===============\n")
        a = float(input("Ingrese número: "))
        b = float(input("Ingrese número: "))
        resultado = a+b
        print("El resultado es: ",resultado)
        input()

    elif (opcion == 2):
        print("===============")
        print("Operación Resta")
        print("===============\n")
        a = float(input("Ingrese número: "))
        b = float(input("Ingrese número: "))
        resultado = a-b
        print("El resultado es: ",resultado)
        input()

    elif (opcion == 3):
        print("========================")
        print("Operación Multiplicación")
        print("========================\n")
        a = float(input("Ingrese número: "))
        b = float(input("Ingrese número: "))
        resultado = a*b
        print("El resultado es: ",resultado)
        input()

    elif (opcion == 4):
        print("=================")
        print("Operación Divisón")
        print("=================\n")
        a = float(input("Ingrese número: "))
        b = float(input("Ingrese número: "))

        if (b == 0):
            print("No se puede dividir por 0")
        else:
            resultado = a/b
            print("El resultado es: ",resultado)
        input()

    elif (opcion == 5):
        print("================================")
        print("Comparación Mayor, menor e igual")
        print("================================\n")
        a = float(input("Ingrese número: "))
        b = float(input("Ingrese número: "))

        if (a > b):
            print("El número ", a, " es mayor que ", b)
        elif (a < b):
            print("El número ", a, " es menor que ", b)
        elif (a == b):
            print("Los números ", a, " son iguales")
        input()

print("Gracias, vuelva pronto")