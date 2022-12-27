# cook your dish here
class TheLastLevel:
    def __init__(self,x,y,z):
        self.x = x 
        self.y = y  
        self.z = z  
        self.level()
        
    def level(self):
        total_time_level = self.x * self.y
        break_time = self.x//3 
        if self.x%3==0:
            time = (break_time - 1)*self.z 
            print(total_time_level + time) 
        else:
            print(total_time_level + break_time*self.z)
            
for i in range(int(input())):
    a,b,c = map(int,input().split())
    t = TheLastLevel(a,b,c)