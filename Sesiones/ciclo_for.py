for iteracion in range (10):
    print(iteracion)
print("========================================")
for iteracion in range (10):
    print(iteracion + 1)
print("========================================")
for iteracion in range (1,11):
    print(iteracion)
print("========================================")

for iteracion in range (1,11,2):
    print(iteracion)

residuo = 5 % 4
print(residuo)
residuo = 4 % 4
print(residuo)
print("========================================")

for iteracion in range (1,11):
    if (iteracion % 2 == 0):
        print(iteracion)
print("========================================")
for iteracion in range (1,11):
    if (iteracion % 2 != 0):
        print(iteracion)
print("========================================")
for iteracion in range (1,11):
    if (iteracion % 2 == 0):
        print(iteracion, "--> Es un número par")
    else:
        print(iteracion, "--> Esun número impar")
print("========================================")
rango = int(input("Ingrese el rango máximo: "))

opcion = int(input('''
    1. Ver solo impares
    2. Ver solo pares
    3. Ver las dos clasificaciones
    n. Cualquier número para mostrar nada

'''))
print("========================================")
if (opcion == 1):
    for iteracion in range (1,rango + 1):
        if (iteracion % 2 != 0):
            print(iteracion)
if (opcion == 2):
    for iteracion in range (1,rango + 1):
        if (iteracion % 2 == 0):
            print(iteracion)
elif (opcion == 3):
    for iteracion in range (1,rango + 1):
        if (iteracion % 2 == 0):
            print(iteracion, "--> Es un número par")
        else:
            print(iteracion, "--> Esun número impar")
else:
    print("Mostrando nada")