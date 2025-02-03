import sys
import os

from pulp import *


PROJECT_ROOT = os.path.abspath(os.path.join( #une rutas
                  os.path.dirname(__file__), #optiene la ruta del archivo __file__ (archivo actual)
                  os.pardir #agrega .. o :: dependiento del sistema operativo
                ))

sys.path.append(PROJECT_ROOT)

prob = LpProblem("Enunciado del Ejercicio 1 Propuesto por Sebastian Arreondo ", LpMinimize)

x= LpVariable("X",0)
y= LpVariable("y",0)


prob += 3*x+2*y, "Z"


prob+=2*x+1*y >= 4, "restriciones1"
prob+=4*x-2*y <=2, "restriciones2"

prob.solve()

for v in prob.variables():
    print(v.name, "=", v.varValue)

print(f"z = {value(prob.objective)}")