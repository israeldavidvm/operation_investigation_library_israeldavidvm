from matplotlib import pyplot
import numpy as np
from shapely import geometry

from math import factorial


class Constraint:
    def __init__(self, coordinates,color="black",label=""):
        self.coordinates = coordinates
        self.color = color
        self.label= label

    def plot(self,axOfSubplots):

        axOfSubplots.plot(*self.coordinates,color=self.color,label=self.label)


def plotConstraints(axOfSubplots,constraints):
    
    for constraint in constraints:

        constraint.plot(axOfSubplots)    

def intersectionCoordinatesOfConstraints(constraints):

    lines=[]
    intersectionsPoints=[]

    for constraint in constraints:

        print(f"constrain {constraint.label}")

        lines.append(geometry.LineString(np.column_stack((constraint.coordinates))))

    combinations=getCombinations(len(lines),2)

    for combination in combinations:

        intersectionPoint=lines[combination[0]].intersection(lines[combination[1]])
        
        if(intersectionPoint.geom_type=='Point'):
            intersectionsPoints.append(intersectionPoint)

    return intersectionsPoints

""" def pointsThatMaxOrMinObjectiveFunction(points,minOrMax="min",function):
    
    

    filter(lambda x: x < 0, lista

    return [point for point in points if function(point.x,point.y)==] """

def getCombinations(n,r):
    
    combinations=[]

    #la primera combinación 
    combination=[element for element in range(0,r)]

    combinations.append(combination[:])
    
    iterationsNumber=1
    while iterationsNumber<=int(factorial(n) / (factorial(r) * factorial(n - r))):
        
        #le asigna al indice la posicion mas a la derecha
        rightIndex = r-1
        val_max = n-1
        
        #inspecciona los elementos desde la derecha hasta que
        #uno no sea el mayor valor posible
        while (combination[rightIndex] == val_max):
            rightIndex = rightIndex-1
            val_max = val_max-1
        
        if rightIndex>-1:
            
            #se incrementa el elemento más a la derecha
            combination[rightIndex] = combination[rightIndex] + 1
        
            #el resto de los elementos son sucesores de combination[rightIndex]
            for j in range(rightIndex + 1, r-1):
                combination[j] = combination[j-1]+1
        
            combinations.append(combination[:])
        
        iterationsNumber+=1

    return combinations


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

intersectionCoordinates=intersectionCoordinatesOfConstraints(constraints[0:4])

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