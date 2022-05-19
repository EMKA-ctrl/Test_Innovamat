from API import API 
from itinerary import itinerary


#Executem fen python challenge.py a la linia de comandes...

professor=API()

activity = professor.nextActivity(itinerary)
print(activity) # Ens retorna la activitat 1

response = {'actId':1,'studentId':1,'Time':90,'Solution':"1_0_2"}
activity = professor.nextActivity(itinerary,activity,response)
print(activity) # 2a

response = {'actId':2,'studentId':1,'Time':15,'Solution':"-2_40_56"}
activity = professor.nextActivity(itinerary,activity,response)
print(activity) # 5a

response = {'actId':5,'studentId':1,'Time':180,'Solution':"0_2_1"}
activity = professor.nextActivity(itinerary,activity,response)
print(activity) # 3a

response = {'actId':3,'studentId':1,'Time':100,'Solution':"1_1"}
activity = professor.nextActivity(itinerary,activity,response)
print(activity) # 3a

response = {'actId':3,'studentId':1,'Time':80,'Solution':"1_0"}
activity = professor.nextActivity(itinerary,activity,response)
print(activity) # 4a







"""

class Student:
    id = None

    def __init__(self,id):
        self.id = id
    def getStudent(self):
        return self.id,self.lastActivity, self.maxActivity
    def newActivity(self):
        #crida a la API per q li retorni next activitat
        

stu = Student(0)
"""



