from pulp import *


"""TOYCO utiliza tres operaciones para armar 3 tipos de juguetes trenes, 
camiones y carros. Los tiempos diarios disponibles para las tres operaciones 
son 430, 460 y 420 minutos, respectivamente, los ingresos por unidad de tren, 
camión y auto de juguete son de $3, $2 y $5 dólares (USD), respectivamente. 
Los tiempos de ensamble por tren en las 3 operaciones son de 1, 3 y 1 minuto, 
respectivamente. Los tiempos correspondientes por camión y por auto son (2,0,4) y (1,2,0) minutos 
un tiempo cero indica que la operación no se utiliza).

Variables de decision:
x1: Numero de trenes
x2: Numero de camiones
x3: Numero de autos

Objetivo del problema: maximizar los ingresos
Función objetivo:
3*x1+2*x2+5*x3

Restricciones:
1*x1+3*x2+1*x3<=430
2*x1+0*x2+4*x3<=460
1*x1+2*x2+0*x3<=420


"""
prob = LpProblem("El Problema de los juguetes Toyco", LpMaximize)

x1= LpVariable("Numero_de_trenes",0)
x2= LpVariable("Numero_de_camiones",0)

prob += 3*x1+2*x2, "Ingresos totales"


prob+=x1 + x2 <= 100, "restriciones_tiempo_operacion_1"
prob+=4*x1 + 6*x2 <= 480, "restriciones_tiempo_operacion_2"
prob+=20*x1 + 10*x2 <= 1500, "restriciones_tiempo_operacion_3"

prob.solve()

for v in prob.variables():
    print(v.name, "=", v.varValue)

print(f"Ingresos totales = {value(prob.objective)}")


