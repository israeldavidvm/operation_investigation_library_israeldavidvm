import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join( #une rutas
                  os.path.dirname(__file__), #optiene la ruta del archivo __file__ (archivo actual)
                  os.pardir #agrega .. o :: dependiento del sistema operativo
                ))

sys.path.append(PROJECT_ROOT)

from operation_investigation_library_israeldavidvm import *

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

variables=[
    ["z","Ingresos Totales"],
    ["x1","Numero de trenes"],
    ["x2","Numero de camiones"],
    ["x3","Numero de automoviles"],
    ["",None] #tyermino independiente
]

coefiObj=LinearExp(variables,np.array([1,-8,-3,-2,0]),"=")

constraints=[
    LinearExp(variables,np.array([0,1,3,1,430]),"<="),
    LinearExp(variables,np.array([0,2,0,4,460]),"<="),
    LinearExp(variables,np.array([0,1,2,0,420]),"<=")
]

modelo=Model(variables,constraints,coefiObj)

modelo.solSimplexMethod("max") 




