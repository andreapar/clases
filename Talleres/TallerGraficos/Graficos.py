#----- Punto 1 -----#
import matplotlib.pyplot as plt

mes = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio"]
ingresos = [100,360,250,230,190,400,312]

plt.bar(mes,ingresos, width= 0.4, color= "m")
plt.title("Niveles de ingresos")
plt.xlabel("Mes")
plt.ylabel("Ingresos")

plt.savefig("GraficoIngresos.png")
plt.show()

#----- Punto 2 -----#
#Gráfica torta con las cuidades

pieLabels = ["Bogotá", "Medellín", "Cali", "Manizales","Cartagena"]
sizes = [7.743,2.529,2.445,4.34,1.028] 
pieExplode = [0, 0.1, 0, 0, 0] 

def etiquetarElementosPorcentuales(sizes, labels, indicador= ' - >'):
    acumulador = 0
    for elemento in sizes :
        acumulador += elemento
    for i in range (len(labels)):
        porcentaje = round (sizes[i] / acumulador * 100 ,2)
        pieLabels[i] += indicador + str(porcentaje) + "%"

etiquetarElementosPorcentuales(sizes, pieLabels,"-")

plt.pie(sizes, labels=pieLabels, explode=pieExplode, shadow= True, counterclock = True, startangle= 43)
plt.title("Población de habitantes en cuidades de Colombia")

plt.savefig("GraficoTortaCiudades.png")
plt.show()

#----- Punto 3 -----#
import pandas as pd

ppgData = pd.read_csv("ppg.csv", encoding="UTF-8", header=0, delimiter= ";").to_dict()
muestras = list (ppgData ["muestra"].values())
voltaje = list (ppgData ["valor"].values())

plt.plot(muestras, voltaje)
plt.title("Fotopletismografía")
plt.xlabel("Tiempo (seg)")
plt.ylabel("Voltaje(mV)")

plt.savefig("GraficoFotopletismografia.png")
plt.show()
