# cook your dish here
class CyclicQuadrilateral:
    
    def __init__(self,a,b,c,d):
        self.a = a 
        self.b = b  
        self.c = c 
        self.d = d 
        self.yes_or_no()
        
    def yes_or_no(self):
        if self.a+self.c == 180 and self.b+self.d == 180:
            print('YES')
        else:
            print('NO')
            
for i in range(int(input())):
    a,b,c,d = map(int,input().split())
    t = CyclicQuadrilateral(a,b,c,d)