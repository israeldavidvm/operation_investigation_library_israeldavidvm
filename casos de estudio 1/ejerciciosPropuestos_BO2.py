from operation_investigation_library_israeldavidvm import *

from matplotlib import pyplot
import numpy as np
from shapely import geometry

from math import factorial

##Inicio de la ejecucion del programa##

xValues=np.arange(0,150,10)
yValues=np.arange(0,150,10)

def objectiveFunction(x,y):
    return 3*x+(2)*y

constraints=[
    Constraint([xValues,(50-(1/2)*xValues)],"y",label="100x+200y<=10000"),
    Constraint([xValues,40-(1/3)*xValues],"b",label="10x+30y<=1200"),
    Constraint([0*yValues,yValues],"orange",label="x>=0"),
    Constraint([xValues,0*xValues],"green",label="y>=0"),
]

fig, ax = pyplot.subplots(layout='constrained')
ax.set_title("Metodo Grafico")  
ax.set_xlabel('Unidades a producir de uvas Sauvignon Blanc')
ax.set_ylabel('Unidades a producir de uvas Chardonay')

plotConstraints(ax,constraints)
 
intersectionCoordinates=[
    intersectionCoordinatesConstraints(constraints[1],constraints[2]),
    intersectionCoordinatesConstraints(constraints[0],constraints[1]),
    intersectionCoordinatesConstraints(constraints[0],constraints[3]),
    intersectionCoordinatesConstraints(constraints[2],constraints[3]),
]

for intersectionCoordinate in intersectionCoordinates:

    ax.plot(intersectionCoordinate.x, intersectionCoordinate.y,  marker='o', markersize=3, color="black")
    
    print(f"Punto de interseccion ({intersectionCoordinate.x}, {intersectionCoordinate.y}) Z={objectiveFunction(intersectionCoordinate.x,intersectionCoordinate.y)}")

ax.fill(
    [intersectionCoordinate.x for intersectionCoordinate 
    in intersectionCoordinates],
    [intersectionCoordinate.y for intersectionCoordinate 
    in intersectionCoordinates], 
    color="silver"
)                   


optimalValue=max([objectiveFunction(coord.x,coord.y) for coord in intersectionCoordinates])

optimalSolCoordinates=[coord for coord in intersectionCoordinates if objectiveFunction(coord.x,coord.y)==optimalValue]

for optimalSolCoordinate in optimalSolCoordinates:

    ax.plot(optimalSolCoordinate.x, optimalSolCoordinate.y,  marker='X', markersize=10, color="blue")

    print(f"La solucion optima es ({optimalSolCoordinate.x}, {optimalSolCoordinate.y}) dando un z={optimalValue}")


ax.legend()
pyplot.show()