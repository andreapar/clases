import funciones as fn
PreguntaNumero = '''Ingrese alguna de estas opciones
    1. Mostrar lista de operaciones
    2. Mostrar listas
    3. Calcular el área de un triángulo
    4. Mostrar topes
    5. Mostrar sucesión de Fibonacci
    6. Salir
'''
listaNum = [12,23,45,67,34,24,56,78,48]

#-----Código-----#
fn.limpiarPantalla()


print("Holaa, espero que estes bien")

opcion = int(input(PreguntaNumero))

while (opcion != 6):
    fn.limpiarPantalla()

    #----- Punto 1 -----#
    if (opcion == 1):
        a = int(input("Por favor ingrese el primer número: "))
        b = int(input("Por favor ingrese el segundo número: "))
        c = int(input("Por favor ingrese el tercer número: "))

        suma = fn.sumar(a, b, c)
        resta = fn.restar(a,b,c)
        multiplicacion  = fn.multiplicar(a,b,c)
        division = fn.dividir(a,b,c)
        potencia1 = fn.potenciar(a,b)
        potencia2 = fn.potenciar(b,c)

        print("El resultadodo de la suma es: ", suma)
        print("El resultadodo de la resta es: ", resta)
        print("El resultadodo de la multiplicación es: ", multiplicacion)
        print("El resultadodo de la división es: ", division)
        print(f"La potencia de {a} a la {b} es: ", potencia1)
        print(f"La potencia de {b} a la {c}  es:", potencia2)
    
    #----- Punto 2 ----#
    elif (opcion == 2):
        profesiones = ["Profesor", "Cantante", "Médico",  "Ingeniero"]
        comida = ["Pizza", "Hamburguesa", "Sushi", "Arroz"]
        flores = ["Margarita", "Rosa", "Ortencia", "Tulipan"]

        fn.mostrarListaMismoTamanho(profesiones, comida, flores)
    
    #----- Punto 3 ----- #
    elif (opcion == 3):
        base= float(input("Por favor ingresa la base en cm: "))
        altura = float(input("Por favor ingresa la altura en cm: "))
        area = fn.calcularArea(base, altura)
        print("El área del triángulo es: ", area)
    
    #----- Punto 4 -----#
    elif (opcion == 4):
        mayor = fn.mayor(listaNum)
        menor = fn.menor(listaNum)
        promedio = fn.promedio(listaNum)

        print("El número más grande es:", mayor)
        print("El número menor es:", menor)
        print("El promedio es:", promedio)
    
    #----- Punto 5 -----#
    elif (opcion == 5):
        numero = int(input("Por favor ingrese el número deseado:"))
        fn.fibonacci(numero)

    fn.pausa()


    fn.limpiarPantalla

    opcion = int(input(PreguntaNumero))

print("Feliz día")