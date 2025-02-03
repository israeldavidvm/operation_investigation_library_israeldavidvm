import sys
import os

from matplotlib import pyplot
import numpy as np
from shapely import geometry

PROJECT_ROOT = os.path.abspath(os.path.join( #une rutas
                  os.path.dirname(__file__), #optiene la ruta del archivo __file__ (archivo actual)
                  os.pardir #agrega .. o :: dependiento del sistema operativo
                ))

sys.path.append(PROJECT_ROOT)

from operation_investigation_library_israeldavidvm import *

##Inicio de la ejecucion del programa##

xValues=np.arange(0,600,10)
yValues=np.arange(0,600,10)

def objectiveFunction(x,y):
    return 5*x+4*y

constraints=[
    Constraint([xValues,500+0*xValues],"b",label="y<=500"),
    Constraint([xValues,1.5*xValues],"r",label="y<=1.5x"),
    Constraint([xValues,600-xValues],"y",label="x+y>=600"),
    Constraint([500+0*yValues,yValues],"purple",label="x<=500"),
    Constraint([xValues,0*xValues],"green",label="y>=0"),
    Constraint([0*yValues,yValues],"orange",label="x>=0"),
]

fig, ax = pyplot.subplots(layout='constrained')
ax.set_title("Metodo Grafico")  
ax.set_xlabel('cantidad de kg de A')
ax.set_ylabel('cantidad de kg de B')

plotConstraints(ax,constraints)

intersectionCoordinates=[
    intersectionCoordinatesConstraints(constraints[0],constraints[1]),
    intersectionCoordinatesConstraints(constraints[0],constraints[3]),
    intersectionCoordinatesConstraints(constraints[2],constraints[3]),
    intersectionCoordinatesConstraints(constraints[1],constraints[2]),
]

for intersectionCoordinate in intersectionCoordinates:

    ax.plot(intersectionCoordinate.x, intersectionCoordinate.y,  marker='o', markersize=3, color="black")
    
    print(f"Punto de interseccion {intersectionCoordinate.x}, {intersectionCoordinate.y}")

ax.fill(
    [intersectionCoordinate.x for intersectionCoordinate 
    in intersectionCoordinates],
    [intersectionCoordinate.y for intersectionCoordinate 
    in intersectionCoordinates], 
    color="silver"
)                   


optimalValue=min([objectiveFunction(coord.x,coord.y) for coord in intersectionCoordinates])

optimalSolCoordinates=[coord for coord in intersectionCoordinates if objectiveFunction(coord.x,coord.y)==optimalValue]

for optimalSolCoordinate in optimalSolCoordinates:

    ax.plot(optimalSolCoordinate.x, optimalSolCoordinate.y,  marker='X', markersize=10, color="blue")

    print(f"La solucion optima para z={optimalValue} es ({intersectionCoordinate.x}, {intersectionCoordinate.y})")


ax.legend()
pyplot.show()