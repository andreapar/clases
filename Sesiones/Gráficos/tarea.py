# Encuesta sobre deportes favoritos 
import matplotlib.pyplot as plt

helado = ["Vainilla", "Chocolate","Caramelo","Cafe", "Ron pasas","Menta"] 
encuesta = [2,3,5,2,1,7]
plt.bar(helado,encuesta,width = 0.4, color= "m")

plt.title("Sabor de helado favoritos")
plt.xlabel("Helado")
plt.ylabel("% de gusto")
plt.show()