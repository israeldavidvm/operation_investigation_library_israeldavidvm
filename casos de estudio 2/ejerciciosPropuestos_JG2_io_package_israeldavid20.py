import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join( #une rutas
                  os.path.dirname(__file__), #optiene la ruta del archivo __file__ (archivo actual)
                  os.pardir #agrega .. o :: dependiento del sistema operativo
                ))

sys.path.append(PROJECT_ROOT)

from operation_investigation_library_israeldavidvm import *

"""
En un laboratorio existen dos contadores de bacterias disponibles. El contador C1 puede ser manipula
do por un estudiante que gana 400 ptas. por hora. En promedio es capaz de contar 5 muestras en una h
ora. El contador C2 es más rápido, pero también más sofisticado. Solo una persona bien preparada per
o que gana 1000 Ptas. Por horapuede manipularlo. Con la misma precisión que C1 el contador C2 permit
e contar 10 muestras en una hora. Al laboratorio se le dan 1000 muestras para que se cuenten en un  
periodo que no exceda las 80 horas ¿Cuántas horas deben usar cada contador para realizar la tarea co
n un coste mínimo? ¿Cuál es el dicho coste?

Variables de decision:
x1 = Cantidad de horas dedicadas a emplear el contador 1
x2 = Cantidad de horas dedicadas a emplear el contador 2

Objetivo del problema: minimizar el coste

Función objetivo:
Min Z = 3x1 + 2x2

Restricciones:

5*x1 + 10x2 = 1000 
x1+x2<=80, 
x1>=0 
x2>=0

"""

variables=[
    ["z","Beneficio"],
    ["x1","Cantidad de horas dedicadas a emplear el contador 1"],
    ["x2","Cantidad de horas dedicadas a emplear el contador 2"],
    ["",None] #tyermino independiente
]

coefiObj=LinearExp(variables,np.array([1,-3,-2,0]),"=")

constraints=[
    LinearExp(variables,np.array([0,5,10,1000]),"="),
    LinearExp(variables,np.array([0,1,1,80]),"<="),
]

modelo=Model(variables,constraints,coefiObj)
modelo.solSimplexMethod("min",10000000)


