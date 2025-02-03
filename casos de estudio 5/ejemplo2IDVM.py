import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join( #une rutas
                  os.path.dirname(__file__), #optiene la ruta del archivo __file__ (archivo actual)
                  os.pardir #agrega .. o :: dependiento del sistema operativo
                ))

sys.path.append(PROJECT_ROOT)

from operation_investigation_library_israeldavidvm import *


# Definimos una lista de tareas y sus tiempos estimados Y las tareas predecesoras de cada tarea
activities=[
    Activity("A", calcMedTime(1,2,3),[],["B","C"]),
    Activity("B", calcMedTime(4,3,8),["A"],["D","E"]),
    Activity("C", calcMedTime(1,3,5),["A"],["E","F","H"]),
    Activity("D", calcMedTime(1,2,3),["B"],["G","H","I"]),
    Activity("E", calcMedTime(6,5,10),["B","C"],["H","I"]),
    Activity("F", calcMedTime(0,1,2),["B","C"],["I"]),
    Activity("G", calcMedTime(3,4,5),["D"],["J","K"]),
    Activity("H", calcMedTime(3,2,7),["E","D","C"],["J","K"]),
    Activity("I", calcMedTime(1,2,3),["D","E","F"],["K"]),
    Activity("J", calcMedTime(5,6,7),["G","H"],["L"]),
    Activity("K", calcMedTime(0.5,1,5),["G","H","I"],["L"]),
    Activity("L", calcMedTime(1,2,3),["J","K"],[]),


]

project=Project(activities)

project.printCriticalPathAnalysis()