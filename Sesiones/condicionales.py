# Constantes
MENSAJE_BIENVENIDA = "Hola, espero que estés bien"
MENSAJE_MAYOR = "El número A es mayor que B"
MENSAJE_MENOR = "El número A es menor que B"
MENSAJE_IGUAL = "Los dos números son iguales"
PREGUNTA_A = "Ingrese un número A: "
PREGUNTA_B = "Ingrese un número B: "

#Código
print(MENSAJE_BIENVENIDA)
numeroA = int(input(PREGUNTA_A))
numeroB = int(input(PREGUNTA_B))
isMayor = numeroA > numeroB
isMenor = numeroA < numeroB
resultado = ""

if (isMayor):
    resultado = MENSAJE_MAYOR
elif (isMenor):
    resultado = MENSAJE_MENOR
else:
    resultado = MENSAJE_IGUAL

print(resultado)
