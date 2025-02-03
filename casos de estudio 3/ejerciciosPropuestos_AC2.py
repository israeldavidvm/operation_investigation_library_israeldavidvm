import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join( #une rutas
                  os.path.dirname(__file__), #optiene la ruta del archivo __file__ (archivo actual)
                  os.pardir #agrega .. o :: dependiento del sistema operativo
                ))

sys.path.append(PROJECT_ROOT)

from operation_investigation_library_israeldavidvm import *

"""
Variables de decision:
x1: 
x2: 
Función objetivo:
+1z-3x1-2x2=+0
Restricciones:
+0z+2x1+1x2>=+80
+0z+1x1+2x2>=+60
"""

prob = LpProblem("Enunciado del Ejercicio 2 Propuesto por alejandro caraballo ", LpMaximize)

x1= LpVariable("X1",0)
x2= LpVariable("X2",0)
x3= LpVariable("X3",0)


prob += 8*x1+3*x2+2*x3, "Ingresos totales"


prob+=-2*x2 + 1*x3 >= 2, "restriciones1"
prob+=1*x1 + -1*x2 +1*x3 ==2, "restriciones2"
prob+=1*x2 + -1*x3 <=1, "restriciones3"


prob.solve()

for v in prob.variables():
    print(v.name, "=", v.varValue)

print(f"z = {value(prob.objective)}")