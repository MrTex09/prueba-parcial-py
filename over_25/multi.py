import matplotlib.pyplot as plt
from over_25_years import over_25_years as o25

def graphics():
    ages = o25()

    # Creamos un gráfico de lineas y le asignamos las edades como variable independiente y las frecuencias como variable dependiente
    plt.plot(ages["Age"], ages["Frequency"], color="blue")

    # Agregamos un encabezado y los labels de ambos ejes
    plt.title("Frecuencia de cada edad")
    plt.xlabel("Edades")
    plt.ylabel("Frecuencia")

    # Agregamos una cuadricula de fondo
    plt.grid(True)

    # Renderizamos el gráfico
    plt.show()

graphics()