import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join( #une rutas
                  os.path.dirname(__file__), #optiene la ruta del archivo __file__ (archivo actual)
                  os.pardir #agrega .. o :: dependiento del sistema operativo
                ))

sys.path.append(PROJECT_ROOT)

from operation_investigation_library_israeldavidvm import *

"""
1.- Un empresario pretende fabricar dos tipos de congeladores denominados A y B. 
Cadauno de ellos debe pasar por tres operaciones antes de su comercialización: Ensamblaje,pintado y control de calidad.
Los congeladores requieren, respectivamente, 2,5 y 3 horasde ensamblaje, 3 y 6 Kg. De esmalte para 
su pintado y 14 y 10 horas de control decalidad. Los costos totales de fabricación por unidad son, r
espectivamente, 30 y 28, y losprecios de venta 52 y 48, todos ellos en miles de pesos. El empresario
disponesemanalmente de 4.500 horas para ensamblaje, de 8.400 Kg. De esmalte y 20.000 horaspara cont
rol de calidad. Los estudios de mercado muestran que la demanda semanal decongeladores no supera las
1.700 unidades y que, en particular, la de tipo A es de, almenos, 600 unidades. Se desea:

a) Formula r un modelo de programación lineal que indique cuántos congeladores debenfabricarse de cada tipo par
a que el beneficio sea máximo, teniendo en cuenta el estudiode demanda.
b) Resolverlo mediante el mét odo simplex. Interpretar la solución óptima incluyendo lasvariables de holgura.
c) Determinar los pre cios sombra de las horas de ensamblaje y control de calidad. Alfabricante le ofrecen disponer de 200 
horas más para ensamblaje con un costo adicionaltotal de $750.000 pesos. ¿Debería aceptar la oferta ?


Variables de decision:
x1 = Cantidad de congeladores de tipo A
x2 = Cantidad de congeladores de tipo B

Objetivo del problema: maximizar el beneficio Beneficio = Ingreso Total - Coste Total

Función objetivo:
Max Z = 3x1 + 2x2

Restricciones:

2.5*x1 + 3*x2 <= 4500 
3x1 + 6x2 <= 8400
14x1 + 10x2 <= 20000 
x1+x2<=1700, 
x1>=600 
x2>=0

"""

variables=[
    ["z","Beneficio"],
    ["x1","Cantidad de congeladores de tipo A"],
    ["x2","Cantidad de congeladores de tipo B"],
    ["",None] #tyermino independiente
]

coefiObj=LinearExp(variables,np.array([1,-3,-2,0]),"=")

constraints=[
    LinearExp(variables,np.array([0,2.5,3,4500]),"<="),
    LinearExp(variables,np.array([0,3,6,8400]),"<="),
    LinearExp(variables,np.array([0,14,10,20000]),"<="),
    LinearExp(variables,np.array([0,1,1,1700]),"<="),
    LinearExp(variables,np.array([0,1,0,600]),">=")
]

modelo=Model(variables,constraints,coefiObj)

modelo.solSimplexMethod("max")


