def calcMedTime(optimistic,probable,pessimistic):
    return (optimistic+4*probable+pessimistic)/6

class Activity(object):
    def __init__(self,tag,duration,predecessors,successors):

        assert duration>=0,f"la duracion debe ser mayor a cero"

        self.tag=tag
        self.duration=duration
        self.predecessors=predecessors
        self.successors=successors

class Project(object):
    def __init__(self,activities):

        self.activities=activities
        self.earlyTimes={}

    def calcEarlyTimes(self):

        self.earlyTimes={}

        for activityIndex in range(0,len(self.activities)):

            self.earlyTimes[self.activities[activityIndex].tag]={}

            if(activityIndex==0):
                self.earlyTimes[self.activities[activityIndex].tag]['start']=0
            else:
                self.earlyTimes[self.activities[activityIndex].tag]['start']= \
                    max(
                        [self.earlyTimes[predecessor]['finish'] 
                        for predecessor in self.activities[activityIndex].predecessors]
                    ) 
                
            
            self.earlyTimes[self.activities[activityIndex].tag]['finish']=\
                self.earlyTimes[self.activities[activityIndex].tag]['start']+self.activities[activityIndex].duration

    def calcLateTimes(self):

            self.lateTimes={}

            for activityIndex in range(len(self.activities) - 1, -1, -1):

                self.lateTimes[self.activities[activityIndex].tag]={}

                if(activityIndex==len(self.activities) - 1):
                    self.lateTimes[self.activities[activityIndex].tag]['finish']=self.earlyTimes[self.activities[activityIndex].tag]['finish']
                else:
                    self.lateTimes[self.activities[activityIndex].tag]['finish']=\
                        min(
                            [self.lateTimes[successor]['start'] 
                            for successor in self.activities[activityIndex].successors]
                        ) 
                    
                
                self.lateTimes[self.activities[activityIndex].tag]['start']=\
                    self.lateTimes[self.activities[activityIndex].tag]['finish']-self.activities[activityIndex].duration

    def calcSlackTimes(self):

        self.slackTimes={}

        for activityIndex in range(0,len(self.activities)):

            self.slackTimes[self.activities[activityIndex].tag]= \
            self.lateTimes[self.activities[activityIndex].tag]['finish']-self.earlyTimes[self.activities[activityIndex].tag]['finish']



    def printCriticalPathAnalysis(self):
        self.calcEarlyTimes()
        self.calcLateTimes()
        self.calcSlackTimes()
        self.printData()
        self.printGraphCriticalPath()
        
    def printData(self):
        for earlyTimeKey,earlyTimeValue in self.earlyTimes.items():
            print(f"tiempo tempranos de la actividad {earlyTimeKey} Inicio:{earlyTimeValue['start']} Fin:{earlyTimeValue['finish']}")
        for lateTimeKey,lateTimeValue in self.lateTimes.items():
            print(f"tiempo tardios de la actividad {lateTimeKey} Inicio:{lateTimeValue['start']} Fin:{lateTimeValue['finish']}")
        for slackTimeKey,slackTimeValue in self.slackTimes.items():
            print(f"tiempo de holgura de la actividad {slackTimeKey} {slackTimeValue}")

        print(f"Tiempo de duracion del proyecto { max([earlyTime['finish'] for earlyTime in self.earlyTimes.values()])}")

         
    def printGraphCriticalPath(self):
        ruta_critica = [slackTimeKey for slackTimeKey,slackTimeValue in self.slackTimes.items() if slackTimeValue == 0]

        print("Ruta crítica:", "->".join(ruta_critica))
        