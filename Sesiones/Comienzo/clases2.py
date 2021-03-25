#En esta clase aprenderemos sobre las variables booleana
pruebaV = True
pruebaF = False
print(pruebaV)
print( pruebaF )
pruebaV = pruebaF
print( pruebaV )

print("-"*16, "Edad", "-"*16)

#Utilizamos el mayor igual para preguntar
edad = 18
estatura = 1.65
peso =  55
nombre = "Andrea Parra"
isMayorEdad = edad >= 18
print(isMayorEdad)

#Utilizamos el signo menor
print("-"*16, "Estatura promedio", "-"*16)
isMayorEstatura = estatura < 1.70
print(isMayorEstatura)

#Acá se utiliza el signo diferente
print("-"*16, "Peso diferente", "-"*16)
isPesoDiferente = peso != 55
print(isPesoDiferente)

#Para preguntar si hay un string en un texto anterior se copia "in"
print("-"*16, "Esta apellido en el nombre", "-"*16)
apellido = "Parra"
isApellido = apellido in nombre
print(isApellido)














