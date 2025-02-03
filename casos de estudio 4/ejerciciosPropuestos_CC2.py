import sys
import os

from pulp import *


PROJECT_ROOT = os.path.abspath(os.path.join( #une rutas
                  os.path.dirname(__file__), #optiene la ruta del archivo __file__ (archivo actual)
                  os.pardir #agrega .. o :: dependiento del sistema operativo
                ))

sys.path.append(PROJECT_ROOT)


prob = LpProblem("Enunciado del Ejercicio 2 Propuesto por cesar casadiego ", LpMinimize)

x1= LpVariable("X1",0)
x2= LpVariable("X2",0)


prob += 3*x1+2*x2, "Z"


prob+=3*x1+1*x2 == 3, "restriciones1"
prob+=4*x1+3*x2 >=6, "restriciones2"
prob+=1*x1+2*x2 <=4, "restriciones3"

prob.solve()

for v in prob.variables():
    print(v.name, "=", v.varValue)

print(f"z = {value(prob.objective)}")