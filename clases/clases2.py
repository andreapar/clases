pruebaV = True
pruebaF = False
print( pruebaV )
print( pruebaF )
pruebaV = pruebaF
print( pruebaV )

print("-"*16, "Edad", "-"*16)

edad = 18
estatura = 1.65
peso =  55
nombre = "Andrea Parra"
isMayorEdad = edad >= 18
print(isMayorEdad)

print("-"*16, "Estatura promedio", "-"*16)
isMayorEstatura = estatura < 1.70
print(isMayorEstatura)

print("-"*16, "Peso diferente", "-"*16)
isPesoDiferente = peso != 55
print(isPesoDiferente)

print("-"*16, "Esta apellido en el nombre", "-"*16)
apellido = "Parra"
isApellido = apellido in nombre
print(isApellido)














