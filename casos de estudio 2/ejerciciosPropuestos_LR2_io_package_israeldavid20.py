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
x1 = ""
x2 = ""

Objetivo del problema: 

Función objetivo:
Max Z = 3x1 + 2x2

Restricciones:

5*x1 + 3*x2 <=15
3*x1 + 5*x2 <=15
x1,x2 >=0


"""

variables=[
    ["z",""],
    ["x1",""],
    ["x2",""],
    ["",None] #tyermino independiente
]

coefiObj=LinearExp(variables,np.array([1,-3,-2,0]),"=")

constraints=[
    LinearExp(variables,np.array([0,5,3,15]),"<="),
    LinearExp(variables,np.array([0,3,5,15]),"<="),
]

modelo=Model(variables,constraints,coefiObj)

modelo.print()

modelo.solSimplexMethod("max")


