import funciones as fn
import random as rd
def sumar(a,b):
    return a + b

print(sumar(2,3))
print(fn.sumar(2,3))
print(fn.calcular(sumar,2,3))

print(rd.randint(2,3))

print(fn.restar(77,56))
print(fn.multiplicar(45,12))
print(fn.dividir(42,6))
print(fn.potenciar(7,7))
