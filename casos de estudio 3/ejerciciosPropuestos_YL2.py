from pulp import *


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
prob = LpProblem("Enunciado del Ejercicio 2 Propuesto por Yesenia Larenas ", LpMinimize)

x1= LpVariable("X1",0)
x2= LpVariable("X2",0)

prob += 3*x1+2*x2, "Ingresos totales"


prob+=2*x1 + 1*x2 >= 80, "restriciones1"
prob+=1*x1 + 2*x2 >= 60, "restriciones2"

prob.solve()

for v in prob.variables():
    print(v.name, "=", v.varValue)

print(f"z = {value(prob.objective)}")


