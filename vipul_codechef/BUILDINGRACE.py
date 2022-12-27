# cook your dish here
#I write this code just to practice oops
class BuildingRace:
    
    def __init__(self,a,b,x,y):
        self.a = a  
        self.b = b  
        self.c = c  
        self.d = d  
        self.race()
        
    def race(self):
        time_a = self.a / self.c
        time_b = self.b / self.d 
        if time_a < time_b:
            print('Chef')
        elif time_a == time_b:
            print('Both')
        else:
            print('Chefina') 
            
for i in range(int(input())):
    a,b,c,d = map(int,input().split())
    t = BuildingRace(a,b,c,d)