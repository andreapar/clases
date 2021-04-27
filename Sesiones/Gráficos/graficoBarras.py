# Aquí explicaremos cómo hacer un gráfico de barras
import matplotlib.pyplot as plt
lenguajes = ["py","java","dart", "ts", "elixir"] 
encuesta = [50,10,20,10,10]
print(lenguajes, encuesta)

plt.bar (lenguajes,encuesta, width = 0.6, color = "c")
##################################
plt.title ("Lenguajes más usados")
plt.xlabel ("Lenguajes de programación")
plt.ylabel ("% de uso de lenguajes")
plt.savefig ("graficoLenguajes.png")
###################################
plt.show()
