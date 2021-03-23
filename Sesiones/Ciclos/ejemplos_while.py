#Entradas
BIENVENIDA = "¡Hola, espero que estés bien!"
MENSAJE_ERROR = "Por favor, ingresa una opción válida"
PREGUNTA_NOMBRE = "Ingresa tu nombre, por favor: "
PREGUNTA_MENU = '''Por favor ingresar
    1. Para mostrar los números del 1 al 5
    2. Para preguntar tu nombre
    3. Para  mostar el año en el que estamos
    4. Salir 
'''

print("========================================")
print(BIENVENIDA)
print("========================================")

#Código
entrada = 1
while (entrada >= 1 and entrada <= 3):
    entrada = int(input(PREGUNTA_MENU))
    if (entrada == 1):
        print(1,2,3,4,5)
    elif (entrada == 2):
        nombre = input(PREGUNTA_NOMBRE)
        print(f"Bievenido {nombre} a este menú")
    elif (entrada == 3):
        print("Estamos en el año 2021")
    elif (entrada == 4):
        print("Muchas gracias, vuelva pronto")
    else:
        entrada = 1
        print(MENSAJE_ERROR)
