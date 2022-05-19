
class API:
    progress=list()

    def score(self,activity,response):
        score=0
        actCorrecta = activity['id'] == response['actId']
        actSol=activity['Solution'].split('_')
        if actCorrecta:
            for index,res in enumerate(response['Solution'].split('_')):
                if res==actSol[index]:
                    score+=1
            
            return int(score*100/len(actSol))
          
    def retorn(self,itinerary,act):
        if itinerary.index(act)-1==len(itinerary):
            return "There are no more available activities, since the itinerary has already been completed !"
        else:
            return act

    def nextActivity(self,itinerary,activity=None,result=None):
        
        if activity is None and result is None:
            return itinerary[0]
        else:
            _score = self.score(activity,result)
            print(str(_score)+'%')
            resTime = result['Time']
            actTime = activity['Time']
            curDiff = activity['Difficulty']

            if _score<20:
                for i,act in enumerate(self.progress[::-1]):
                    if act['Difficulty']==curDiff-1:
                        return self.retorn(itinerary,itinerary[itinerary.index(act)+1])

            elif _score<75:
                return itinerary[activity['id']-1]

            elif _score>75 and resTime<(0.5*actTime):
                if activity not in self.progress:
                    self.progress.append(activity)
                for act in itinerary:
                    if act['Difficulty']==curDiff+1:
                        return self.retorn(itinerary,act)

            elif _score>75 and not(resTime<(0.5*actTime)):
                if activity not in self.progress:
                    self.progress.append(activity)
                return self.retorn(itinerary,itinerary[activity['id']])
            


    
"""
Solució 3.1
if _score<75:
            return itinerary[activity['id']-1]
        else:
            return itinerary[activity['id']]
"""

    

