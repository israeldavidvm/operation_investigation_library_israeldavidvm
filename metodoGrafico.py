from matplotlib import pyplot
import numpy as np
from shapely import geometry

class Constraint:
    def __init__(self, coordinates,color="black",label=""):
        self.coordinates = coordinates
        self.color = color
        self.label= label

    def plot(self,axOfSubplots):

        axOfSubplots.plot(*self.coordinates,color=self.color,label=self.label)

def intersectionCoordinatesConstraints(constraint1,constraint2):

    constraint1Line=geometry.LineString(np.column_stack((constraint1.coordinates)))
    constraint2Line=geometry.LineString(np.column_stack((constraint2.coordinates)))

    return constraint1Line.intersection(constraint2Line)

def plotConstraints(axOfSubplots,constraints):
    
    for constraint in constraints:

        constraint.plot(axOfSubplots)    

