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

variables=[
    ["z",""],
    ["x1",""],
    ["x2",""],
    ["",None] #tyermino independiente
]

coefiObj=LinearExp(variables,np.array([1,-3,-2,0]),"=")

constraints=[
    LinearExp(variables,np.array([0,3,2,5]),"="),
    LinearExp(variables,np.array([0,4,1,6]),">="),
    LinearExp(variables,np.array([0,1,1,3]),"<="),
]

modelo=Model(variables,constraints,coefiObj)

modelo.solSimplexMethod("max",10000000)


