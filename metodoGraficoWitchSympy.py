from matplotlib import pyplot
import numpy

from sympy import plot_implicit, symbols, Eq, And

from optlang import Model, Variable, Constraint, Objective


class Constraint:
    def __init__(self, coordinates,color="black"):
        self.coordinates = coordinates
        self.color = color


def objectiveFunction(x,y):
    return 5*x+4*y

def print_constraints(axOfSubplots,constraints):
    
    for constraint in constraints:

        axOfSubplots.plot(*constraint.coordinates,color=constraint.color,label="")
    

def intersectionCoordinatesOfConstraints():
    first_line = geometry.LineString(np.column_stack((xValues, y1)))
    first_line = geometry.LineString(np.column_stack((xValues, y1)))

    intersection = first_line.intersection(second_line)

x, y = symbols('x y')
p1 = plot_implicit(y - 1>0, y_var=y)

constraints=[
    Constraint([z500+0*x],"b"),
    Constraint([xValues,1.5*xValues],"r"),
    Constraint([xValues,600-xValues],"y"),
    Constraint([xValues,0*xValues],"green"),

    Constraint([500+0*yValues,yValues],"purple"),
    Constraint([0*yValues,yValues],"orange"),
]

fig, ax = pyplot.subplots(layout='constrained')
ax.set_title("Metodo Grafico")  
ax.set_xlabel('cantidad de kg de A')
ax.set_ylabel('cantidad de kg de B')

print_constraints(ax,constraints)

ax.legend();  


pyplot.show()

# All the (symbolic) variables are declared, with a name and optionally a lower and/or upper bound.
x = Variable('x1', lb=0)
y = Variable('x2', lb=0)

# A constraint is constructed from an expression of variables and a lower and/or upper bound (lb and ub).
c1 = Constraint(x1 + x2 + x3, ub=100)
c2 = Constraint(10 * x1 + 4 * x2 + 5 * x3, ub=600)
c3 = Constraint(2 * x1 + 2 * x2 + 6 * x3, ub=300)

# An objective can be formulated
obj = Objective(10 * x1 + 6 * x2 + 4 * x3, direction='max')

# Variables, constraints and objective are combined in a Model object, which can subsequently be optimized.
model = Model(name='Simple model')
model.objective = obj
model.add([c1, c2, c3])
status = model.optimize()
print("status:", model.status)
print("objective value:", model.objective.value)
print("----------")
for var_name, var in model.variables.items():
    print(var_name, "=", var.primal)
