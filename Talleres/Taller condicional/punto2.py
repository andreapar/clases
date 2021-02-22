#PUNTO2. Pida la edad del usuario y muestre en pantalla la siguiente información:
#Si tiene menos de 18 años diga que es menor de edad
#Desde 18 hasta 25 Es Joven
#Desde 26 hasta 60 Adulto
# Mayor a 60 años es Adulto mayor

# #Constantes
PREGUNTA_EDAD = "Por favor ingresa tu edad: "
MENSAJE_MENOR_EDAD = "Eres menor de edad, todavía tienes mucho por delante"
MENSAJE_JOVEN = "Eres joven, estas en la mejor etapa"
MENSAJE_ADULTO = "Eres adulto, recuerda, tomar agua y dormir"
MENSAJE_ADULTO_MAYOR = "Eres adulto mayor, haz vivido mucho"

#Código
edad = int(input(PREGUNTA_EDAD))
isMenorEdad = edad < 18
isJoven = edad >= 18 and edad < 25
isAdulto = edad >= 26 and edad < 60
isMayorAdulto = edad >= 60

if (isMenorEdad):
    print(MENSAJE_MENOR_EDAD)
elif (isJoven):
    print(MENSAJE_JOVEN)
elif (isAdulto):
    print(MENSAJE_ADULTO)
else:
    print(MENSAJE_ADULTO_MAYOR)

input()
