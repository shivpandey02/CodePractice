# cook your dish here
#I write thos code just practice of oops 
class MarioAndBullet:
    def __init__(self):
        time = int(input())
        for i in range(time):
            x,y,z = map(int,input().split())
            self.x = x  
            self.y = y   
            self.z = z   
            print(int(self.least()))
            
    def least(self):
        t = self.y/self.x 
        if t>self.z:
            return '0'
        return self.z - t
        
M = MarioAndBullet()