from operation_investigation_library_israeldavidvm import *

from matplotlib import pyplot
import numpy as np
from shapely import geometry

from math import factorial

##Inicio de la ejecucion del programa##

xValues=np.arange(0,15,0.1)
yValues=np.arange(0,15,0.1)

def objectiveFunction(x,y):
    return 3*x+(2)*y

constraints=[
    Constraint([xValues,(8-xValues)],"y",label="2x+2y<=16"),
    Constraint([xValues,6-0.5*xValues],"b",label="x+2y<=12"),
    Constraint([4.66+0*yValues,yValues],"r",label="x<=4.66"),
    Constraint([0*yValues,yValues],"orange",label="x>=0"),
    Constraint([xValues,0*xValues],"green",label="y>=0"),
]

fig, ax = pyplot.subplots(layout='constrained')
ax.set_title("Metodo Grafico")  
ax.set_xlabel('Unidades a producir del producto 1 semanalmente')
ax.set_ylabel('Unidades a producir del producto 2 semanalmente')

plotConstraints(ax,constraints)

intersectionCoordinates=[
    intersectionCoordinatesConstraints(constraints[3],constraints[4]),
    intersectionCoordinatesConstraints(constraints[3],constraints[1]),
    intersectionCoordinatesConstraints(constraints[1],constraints[0]),
    intersectionCoordinatesConstraints(constraints[0],constraints[2]),
    intersectionCoordinatesConstraints(constraints[2],constraints[4]),

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