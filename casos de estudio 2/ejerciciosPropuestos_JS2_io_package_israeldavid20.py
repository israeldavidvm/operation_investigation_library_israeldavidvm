import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join( #une rutas
                  os.path.dirname(__file__), #optiene la ruta del archivo __file__ (archivo actual)
                  os.pardir #agrega .. o :: dependiento del sistema operativo
                ))

sys.path.append(PROJECT_ROOT)

from operation_investigation_library_israeldavidvm import *

"""
Un granjero posee 100 hectáreas para cultivar trigo y alpiste. 
El costo de la semilla de trigo es de $4 por hectárea y la semilla de alpiste tiene un coste de 
$6 por hectárea. El coste total de mano de obra es de $20 y $10 por  hectárea respectivamente. 
La utilidad neta esperada es de $110 por hectárea de trigo y $150 por hectárea de alpiste. 
Si no se desea gastar más de $480 en semillas ni mas de $1500 en mano de obra. 
¿Cuántas hectáreas de cada uno de los cultivos debe plantarse para obtener la maxima ganancia?

Variables de decision:
X = Cantidad de hectareas de trigo
Y = Cantidad de hectareas de alpiste

Objetivo del problema: maximizar la ganancia

Función objetivo:
Max Z = 3X + 2Y

Restricciones:

X + Y <= 100 (Hectareas disponibles)
4X + 6Y <= 480 (Costo de semillas)
20X + 10Y <= 1500 (Mano de obra)

"""

variables=[
    ["z","Ganancia"],
    ["x1","Cantidad de hectareas de trigo"],
    ["x2","Cantidad de hectareas de alpiste"],
    ["",None] #tyermino independiente
]

coefiObj=LinearExp(variables,np.array([1,-3,-2,0]),"=")

constraints=[
    LinearExp(variables,np.array([0,1,1,100]),"<="),
    LinearExp(variables,np.array([0,4,6,480]),"<="),
    LinearExp(variables,np.array([0,20,10,1500]),"<=")
]

modelo=Model(variables,constraints,coefiObj)

modelo.solSimplexMethod("max")


