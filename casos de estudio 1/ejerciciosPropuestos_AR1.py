from operation_investigation_library_israeldavidvm import *

from matplotlib import pyplot
import numpy as np
from shapely import geometry

##Inicio de la ejecucion del programa##

xValues=np.arange(0,36000,10)
yValues=np.arange(0,36000,10)

def objectiveFunction(x,y):
    return 3*x+(4)*y

constraints=[
    Constraint([xValues,(9000-((3/4)*xValues))],"y",label="3x+4y>=36000"),
    Constraint([xValues,xValues],"b",label="x>=y"),
    Constraint([20+0*yValues,yValues],"r",label="x<=20"),
    Constraint([xValues,10+0*xValues],"purple",label="y<=10"),
    Constraint([0*yValues,yValues],"orange",label="x>=0"),
    Constraint([xValues,0*xValues],"green",label="y>=0"),
]

fig, ax = pyplot.subplots(layout='constrained')
ax.set_title("Metodo Grafico")  
ax.set_xlabel('Cantidad de coches vendidos del modelo A')
ax.set_ylabel('Cantidad de coches vendidos del modelo B')

plotConstraints(ax,constraints)

print("no hay solucion, es decir no hay ningun \
par ordenado que satisfaga las restricciones\n")

ax.legend()
pyplot.show()
