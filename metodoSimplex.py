from pulp import *

import numpy as np
import pandas as pd

class Model(object):
    def __init__(self,variables,constraints,objetiveFuction):

        self.variables=variables
        self.constraints=constraints
        self.objetiveFunction=objetiveFuction

    def transformStandartForm(self,objetive,bigM):

        self.basicVariables=[]

        self.basicVariables.append(self.variables[0][0])

        for i in range(0,len(self.constraints)):
            if(self.constraints[i].sig=="<="):
                newVar=["h"+str(i+1),None]

                self.addVariable(newVar)

                self.objetiveFunction.addVariable(newVar,coefi=0)
                self.basicVariables.append(newVar[0])

                self.constraints[i].sig=="="


                print(f"Como la restricción {i+1} es del tipo '≤' se agrega la variable de holgura {newVar[0]}.")
                
                for j in range(0, len(self.constraints)):

                    if(i==j):
                        self.constraints[j].addVariable(newVar,coefi=1)
                    else:
                        self.constraints[j].addVariable(newVar,coefi=0)
            
            if(self.constraints[i].sig=="="):
                newVar=["a"+str(i+1),None]
                self.addVariable(newVar)
                self.basicVariables.append(newVar[0])

                self.objetiveFunction.addVariable(newVar,coefi=bigM)

                self.constraints[i].sig=="="

                print(f"Como la restricción {i+1} es del tipo '=' se agrega la variable artificial {newVar[0]}.")
                
                for j in range(0, len(self.constraints)):

                    if(i==j):
                        self.constraints[j].addVariable(newVar,coefi=1)
                    
                        if(objetive=="max"):

                            self.objetiveFunction.coefiLinearExp=self.objetiveFunction.coefiLinearExp-bigM*self.constraints[i].coefiLinearExp
                        
                        elif(objetive=="min"):

                            self.objetiveFunction.coefiLinearExp=self.objetiveFunction.coefiLinearExp+bigM*self.constraints[i].coefiLinearExp

                    
                    else:
                        self.constraints[j].addVariable(newVar,coefi=0)

            if(self.constraints[i].sig==">="):
                newVar1=["e"+str(i+1),None]
                newVar2=["a"+str(i+1),None]

                self.addVariable(newVar1)
                self.addVariable(newVar2)

                self.basicVariables.append(newVar2[0])

                self.objetiveFunction.addVariable(newVar1,coefi=0)
                self.objetiveFunction.addVariable(newVar2,coefi=bigM)

                self.constraints[i].sig=="="

                print(f"Como la restricción {i+1} es del tipo '>=' se agrega la variable exceso {newVar1[0]}.")
                print(f"Como la restricción {i+1} es del tipo '>=' se agrega la variable artificial {newVar2[0]}.")

                
                for j in range(0, len(self.constraints)):

                    if(i==j):
                        self.constraints[j].addVariable(newVar1,coefi=-1)
                        self.constraints[j].addVariable(newVar2,coefi=1)

                        if(objetive=="max"):

                            self.objetiveFunction.coefiLinearExp=self.objetiveFunction.coefiLinearExp-bigM*self.constraints[i].coefiLinearExp
                        
                        elif(objetive=="min"):

                            self.objetiveFunction.coefiLinearExp=self.objetiveFunction.coefiLinearExp+bigM*self.constraints[i].coefiLinearExp


                    else:
                        self.constraints[j].addVariable(newVar1,coefi=0)
                        self.constraints[j].addVariable(newVar1,coefi=0)


    
    def addVariable(self,variable):
        independentTerm=self.variables[-1]
        self.variables=self.variables[:-1]
        self.variables.append(variable)
        self.variables.append(independentTerm)

    def print(self):
        print("Variables de decision:")
        self.printVariablesDecision()
        print("Función objetivo:")
        print(self.objetiveFunction)
        print("Restricciones:")
        self.printConstraints()

    def printVariablesDecision(self):

        for variable in self.variables[1:]:
            if(variable[1]!=None):
                print(f"{variable[0]}: {variable[1]}")

    def printConstraints(self):

        for constraint in self.constraints:
            print(constraint)

    def solSimplexMethod(self,objetive="max", bigM=10000):

        self.print()

        print("Pasamos el problema a la forma estándar,añadiendo variables de exceso, holgura, y artificiales según corresponda")
        self.transformStandartForm(objetive,bigM)
        self.print()
       
        coefis=[]
        
        if(objetive=="min"):
            coefis.append(self.objetiveFunction.coefiLinearExp*-1)
        else:
            coefis.append(self.objetiveFunction.coefiLinearExp)
        
        for constraint in self.constraints:
            coefis.append(constraint.coefiLinearExp)
            
        self.printTable(coefis,self.basicVariables,"tabla.csv")

        while(self.canBeOptimized(coefis[0])):

            indexInputVar=self.getIndexInputVariable(coefis[0])

            indexOutputVar=self.getIndexOutputVariable(coefis,indexInputVar)

            print(indexOutputVar,indexInputVar)

            self.basicVariables[indexOutputVar]=self.variables[indexInputVar][0]

            if(indexOutputVar==-1):

                print("Este problema arroja una solucion no acotada")
                raise Exception("solucion no acotada")

            self.columnElimination([indexInputVar,indexOutputVar],coefis)

            self.printTable(coefis,self.basicVariables,"tabla.csv")

        #if(self.canItBeAMultipleSolution(coefiObjetiveFunction=coefis[0])):
        #    print("Esta es una solucion optima, pero muchas mas pues este es el caso de una solucion multiple")
        
        # print("lo que es igual a ")

        # for constraint in coefis[:]:
        #     LinearExp(self.variables,np.array(constraint),"=").printwithoutZeros()

        #imprime el valor de cada variable basica

        basicVariablesAndTheirValues=self.getBasicVariablesAndTheirValues(coefis)

        if(self.isValidTheSolution(basicVariablesAndTheirValues)):

            for basicVariableAndTheirValue in basicVariablesAndTheirValues:

                print(f"{basicVariableAndTheirValue[0]}={basicVariableAndTheirValue[1]}")
        else:

            print("No existe una solucion factible para este problema")

    
    def getBasicVariablesAndTheirValues(self,coefis):
        
        basicVariablesAndTheirValues=[]
        
        for i in range(0, len(self.basicVariables)):
            
            indexBasicVariable=self.getIndexBasicVariable(self.basicVariables[i])
            
            valueBasicVariable=coefis[i][-1]/coefis[i][indexBasicVariable]

            basicVariablesAndTheirValues.append((self.basicVariables[i],valueBasicVariable))

        return basicVariablesAndTheirValues

    def getIndexBasicVariable(self,basicVariable):
        for index  in range(0,len(self.variables)):
            if (self.variables[index][0]==basicVariable):
                return index

        return -1

    def printTable(self,coefis,basicVariables,logFile=None):

        df = pd.DataFrame(coefis,columns=[var[0] for var in self.variables])
        basicVariablesDataframe = pd.DataFrame(
            {'Variables Basicas': basicVariables}, columns = ['Variables Basicas']
        )
        df = pd.concat([basicVariablesDataframe,df], axis=1,)

        print(df)

        if(logFile!=None):

            df.to_csv(logFile,mode="a")


    def columnElimination(self,pivoteIndices,coefis):

        #print(pivoteIndices,coefis[pivoteIndices[1]])

        coefiPivote=coefis[pivoteIndices[1]][pivoteIndices[0]]

        if(coefiPivote!=0):

            coefis[pivoteIndices[1]]=coefis[pivoteIndices[1]]/coefiPivote

        for f in range(0,len(coefis)):

            if(f==pivoteIndices[1]):
                continue

            coefiRow=coefis[f][pivoteIndices[0]]

            coefis[f]=coefis[f]-(coefis[pivoteIndices[1]]*coefiRow)
            

    def canBeOptimized(self,coefiObjetiveFunction):

        for coefi in coefiObjetiveFunction[1:-1]:

            if (coefi<0):
                return True

        return False

    def isValidTheSolution(self, solution):
        """
        la condicion de solucion no factible se manifiesta en el metodo simplex
        cuando una variable artificial aparece en una base optima con un valor positivo
        return  False si hay alguna variable artificial >0
        """


        for var in solution:

            varName=var[0]
            varValue=var[1]

            firstLetter=varName[0]

            if(firstLetter=="a" and varValue>0):

                return False

        return True


    def canItBeAMultipleSolution(self,coefiObjetiveFunction):

        """
        En un problema de PL se presenta una solucion optima multiple cuando
        se encontro una solucion optima y adeams el coeficiente de la fila cero para una variable no basica 
        es igual a cero

        Returns:
            _type_: _description_
        """

        #se escluye el coeficiente de z y el del termino independiente
        for i in range(1,len(coefiObjetiveFunction)-1):
        
            if(coefiObjetiveFunction[i]==0):
                return True
            else: 
                return False
        
    
    def getIndexInputVariable(self,coefiObjetiveFunction):
        """
        En el caso de una solucion multiple se muestra una advertencia pero se sige con 
        el flujo estandar, es decir se busca la primera solucion optima
        En caso de que alla un empate de la variable basica entrante:
        retorna el indice de la primera evaluando de izuierda aderecha
        En otro caso:
        Retorna el indice de la variable entrante,  

        Args:
            coefiObjetiveFunction (_type_): _description_
            objetive (str, optional): _description_. Defaults to "max".

        Returns:
            _type_: _description_
        """

        index=-1

        coefiInputVariable=None

        #se escluye el coeficiente de z y el del termino independiente
        for i in range(1,len(coefiObjetiveFunction)-1):

            #notese que en caso de empate tanto para minimo como maximo
            #se escoge el primero que sea minimo o maximo, los demas indices que cumplan con
            #esta caracteristica se ignoran
            if(coefiInputVariable==None or (coefiObjetiveFunction[i]<coefiInputVariable)):
                index=i
                coefiInputVariable=coefiObjetiveFunction[i]

        
        return index
    
    def getIndexOutputVariable(self,coefis,indexInputVariable):
        """
        En caso de degeneracion (existe mas de una variable de salida):
            Se retorna la primera evaluado de arriba abajo y se imprime una dvertensia
        En caso de Z no acotada(no hay variable de salida):
            Se retorna -1
        En otro caso:
            Se retorna el indice de la variable de salida,

        Args:
            coefis (_type_): _description_
            indexInputVariable (_type_): _description_
            objetive (str, optional): _description_. Defaults to "max".

        Raises:
            Exception: _description_

        Returns:
            _type_: _description_
        """

        index=-1
        cociente=None
        newCociente=None

        for f in range(1,len(coefis)):

            if(
                coefis[f][indexInputVariable]!=0 and 
                (coefis[f][-1]/coefis[f][indexInputVariable])>0
            ):
            
                newCociente=(coefis[f][-1])/(coefis[f][indexInputVariable])                

            
            if(newCociente==cociente):
                print("cuidado parece que se a producido una degeneeracion \
                    (hay mas de una variable basica de salida) en algunos casos \
                        puede ser que se caiga en un bucle infinito"
                )



            if(
                cociente==None or newCociente<cociente
            ):

                cociente=newCociente

                if(cociente!=None):

                    index=f
        
        return index

            
    


class LinearExp(object):

    def __init__(self,variables,coefiLinearExp,sig=None):

        if(sig!="=" and sig!="<=" and sig!=">="):
            raise Exception("una expresion lineal solo puede ser una ecuacion o inecuacion")

        self.sig=sig
        
        self.variables=[var[0] for var in variables]
        
        self.coefiLinearExp=np.around(coefiLinearExp,3)

    def addVariable(self,variable,coefi):

        independentTerm=self.variables[-1]
        self.variables=self.variables[:-1]
        self.variables.append(variable[0])
        self.variables.append(independentTerm)

        self.coefiLinearExp=np.concatenate((self.coefiLinearExp[:-1],[coefi],[self.coefiLinearExp[-1]]))

    def __str__(self):
        string=""

        for i in range(0,len(self.coefiLinearExp)):

            if(i==len(self.coefiLinearExp)-1):
                string+=self.sig

            if(self.coefiLinearExp[i]>=0):

                string+=f"+{str(self.coefiLinearExp[i])}{self.variables[i]}"    
            
            else:

                string+=f"{str(self.coefiLinearExp[i])}{self.variables[i]}"

        return string

    def printwithoutZeros(self):
        string=""

        for i in range(0,len(self.coefiLinearExp)):

            if(self.coefiLinearExp[i]>=0):


                if(i==len(self.coefiLinearExp)-1):
                    string+="="

                if(self.coefiLinearExp[i]==0):
                    continue

                string+=f"+{str(self.coefiLinearExp[i])}{self.variables[i]}"    
            
            else:

                string+=f"{str(self.coefiLinearExp[i])}{self.variables[i]}"

        print(string)

