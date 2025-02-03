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
x1, x2, x3

Función objetivo:
+1z-8x1-3x2-2x3=0

Restricciones:
1x1+2x2-1x3<=+7
-1x1+1x2-2x3<=-5
1x1+4x2+3x3>=+1
2x1-1x2+4x3=+6

"""

variables=[
    ["z",""],
    ["x1",""],
    ["x2",""],
    ["x3",""],
    ["",None] #tyermino independiente
]

coefiObj=LinearExp(variables,np.array([1,-8,-3,-2,0]),"=")

constraints=[
    LinearExp(variables,np.array([0,1,2,-1,7]),"<="),
    LinearExp(variables,np.array([0,-1,1,-2,-5]),"<="),
    LinearExp(variables,np.array([0,1,4,3,1]),">="),
    LinearExp(variables,np.array([0,2,-1,4,6]),"=")
]

modelo=Model(variables,constraints,coefiObj)

modelo.solSimplexMethod("max")


