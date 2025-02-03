from operation_investigation_library_israeldavidvm import *

from matplotlib import pyplot
import numpy as np
from shapely import geometry

from math import factorial

##Inicio de la ejecucion del programa##

xValues=np.arange(0,1000,10)
yValues=np.arange(0,1000,10)

def objectiveFunction(x,y):
    return 3*x+(2)*y

constraints=[
    Constraint([550+0*yValues,yValues],"b",label="x>=550"),
    Constraint([xValues,580+0*xValues],"r",label="y>=580"),
    Constraint([800+0*yValues,yValues],"y",label="x<=800"),
    Constraint([xValues,600+0*xValues],"green",label="y<=600"),
    Constraint([0*yValues,yValues],"black",label="x>=0"),
    Constraint([xValues,0*xValues],"black",label="y>=0"),
]

fig, ax = pyplot.subplots(layout='constrained')
ax.set_title("Metodo Grafico")  
ax.set_xlabel('Cantidad de laminas de aluminio')
ax.set_ylabel('Cantidad de varillas de aluminio')

plotConstraints(ax,constraints)
 
intersectionCoordinates=[
    intersectionCoordinatesConstraints(constraints[0],constraints[3]),
    intersectionCoordinatesConstraints(constraints[3],constraints[2]),
    intersectionCoordinatesConstraints(constraints[2],constraints[1]),
    intersectionCoordinatesConstraints(constraints[0],constraints[1]),
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