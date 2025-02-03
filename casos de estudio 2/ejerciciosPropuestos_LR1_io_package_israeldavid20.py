import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join( #une rutas
                  os.path.dirname(__file__), #optiene la ruta del archivo __file__ (archivo actual)
                  os.pardir #agrega .. o :: dependiento del sistema operativo
                ))

sys.path.append(PROJECT_ROOT)

from operation_investigation_library_israeldavidvm import *

"""
Weenies and Buns es una planta procesadora de alimentos que fabrica hotdogs y pan para hotdogs. 
Muele su propia harina para el pan a una tasa máxima de 200 libras por semana. 
Cada pan requiere 0.1 libras. Tienen un contrato con pigland, Inc., 
que especifica la entrega de 800 libras de productos de puerco cada lunes. 
Cada hotdog requiere de 1/4 de libra de producto de puerco. Se cuenta con suficiente cantidad 
del resto de los ingredientes de ambos productos. 
Por último, la mano de obra consiste en 5 empleados de tiempo completo (40 horas por semana). 
Cada Hotdogs requiere 3 minutos de mano de obra y cada pan de 2 minutos de mano de obra. 
Cada hotdog proporciona una ganancia de $0.8 y cada pan de $0.30. 

Weenies and Buns desea saber cuántos hotdogs cuantos panes deben producir cada semana para lograr la ganancia más alta posible

Variables de decision:
x1 = Cantidad de panes producidos
x2 = Cantidad de hotdogs producidos

Objetivo del problema: 

Función objetivo:
Max Z = 3x1 + 2x2

Restricciones:

0.1*x1<=200
1/4*x2<=800
2*x1 + 3*x2 <= 5*40*60=12000


"""

variables=[
    ["z","Beneficio"],
    ["x1","Cantidad de panes producidos"],
    ["x2","Cantidad de hotdogs producidos"],
    ["",None] #tyermino independiente
]

coefiObj=LinearExp(variables,np.array([1,-3,-2,0]),"=")

constraints=[
    LinearExp(variables,np.array([0,(1/10),0,200]),"<="),
    LinearExp(variables,np.array([0,0,(1/4),800]),"<="),
    LinearExp(variables,np.array([0,2,3,12000]),"<=")
]

modelo=Model(variables,constraints,coefiObj)
modelo.solSimplexMethod("max")


