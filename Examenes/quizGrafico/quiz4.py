import pandas as pd
import matplotlib.pyplot as plt

# Quiz de gráficos

#----- Punto 1 -----#
listaSnacks = []
listaPrecios = []
for i in range (5):
    snack = input("Por favor ingrese un snack: ")
    precio = input("Ingrese el precio de el snack: ")
    listaPrecios.append (precio)
    listaSnacks.append (snack)

print (listaSnacks)
print (listaPrecios)
print("========================================================================")

plt.bar (listaSnacks,listaPrecios, width= 0.6, color = "c")
plt.title("Precio de los Snack favoritos")
plt.xlabel("Snacks")
plt.ylabel("Precio")

plt.savefig("GraficoSnackFav.png")
plt.show()

#----- Punto 2 -----#
listaCiudades = []
listaPoblaciones = []
for i in range (5):
    ciudad = input("Por favor ingrese una ciudad: ")
    poblacion = input("Por favor ingrese el número de población de esta ciudad: ")
    listaCiudades.append (ciudad)
    listaPoblaciones.append (poblacion)

print (listaCiudades)
print (listaPoblaciones)
maximo = listaPoblaciones.index(max(listaPoblaciones))
pieExplode = [0,0,0,0,0]

pieExplode [maximo]= 0.2

plt.pie(listaPoblaciones, labels=listaCiudades, explode= pieExplode)
plt.title("Población de las ciudades favoritas")

plt.savefig("GraficoCiudades.png")
plt.show()

#----- Punto 3 -----#
print('''------------------------------------------
Un fotopletismograma (PPG) es un pletismograma obtenido ópticamente.
Un PPG a menudo se obtiene mediante el uso de un oxímetro de pulso
que ilumina la piel y mide los cambios en la absorción de la luz
------------------------------------------''')

ppgData = pd.read_csv("ppg.csv", encoding="UTF-8", header=0, delimiter= ";").to_dict()
muestras = list (ppgData ["muestra"].values())
voltaje = list (ppgData ["valor"].values())

plt.plot(muestras, voltaje)
plt.title("Fotopletismografía")
plt.xlabel("Tiempo (seg)")
plt.ylabel("Voltaje(mV)")

plt.savefig("GraficoFotopletismografia.png")
plt.show()

#Ecg
print('''------------------------------------------
Un electrocardiograma es una prueba que mide la actividad del corazón.
En una prueba de esfuerzo durante el ejercicio,
tiene un ECG mientras camina o trota en una caminadora
------------------------------------------''')

ecgData = pd.read_csv("ecg.csv",encoding="UTF-8",header=0,delimiter=';').to_dict()
muestras = list(ecgData["muestra"].values())
voltaje = list(ecgData["valor"].values())

plt.plot(muestras, voltaje)
plt.title("Electrocardiograma")
plt.xlabel("Muestra")
plt.ylabel("Valor(mV)")

plt.savefig("Electrocardiograma.png")
plt.show()