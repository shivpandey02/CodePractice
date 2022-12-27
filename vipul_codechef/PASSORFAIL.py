# cook your dish here
#I write this code for just pratice of oop 
class PassFail:
    
    def __init__(self,x,y,z):
        self.x = x 
        self.y = y  
        self.z = z 
        self.pass_or_fail()
        
    def pass_or_fail(self):
        w = self.x - self.y  
        c = self.y*3 - w 
        if c >= self.z:
            print('PASS')
        else:
            print('FAIL')
        
        
for i in range(int(input())):
    a,b,c = map(int,input().split())
    t = PassFail(a,b,c)
