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
    Activity("A", 2,[],["B","C","D"]),
    Activity("B", 1,["A"],["E"]),
    Activity("C", 2,["A"],["E"]),
    Activity("D", 0.5,["A"],["E"]),
    Activity("E", 4,["B","C"],[]),
]

project=Project(activities)

project.printCriticalPathAnalysis()