# cook your dish here
class ValidTriangles:
    
    def __init__(self,a,b,c):
        self.a = a 
        self.b = b 
        self.c = c 
        self.valid()
        
    def valid(self):
        sum = self.a + self.b + self.c 
        if sum == 180:
            print('YES')
        else:
            print('NO')
        
for i in range(int(input())):
    a,b,c = map(int,input().split())
    ValidTriangles(a,b,c)