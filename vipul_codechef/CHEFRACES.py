# cook your dish here
#I write this code in oops just for practice
class ChefRaces:
    
    def __init__(self,a,b,c,d):
        self.a = a   
        self.b = b 
        self.c = c   
        self.d = d 
        self.no_of_medal()
        
    def no_of_medal(self):
        count = 0
        l = [self.a,self.b]
        k = [self.c,self.d]
        for i in l:
            if i not in k:
                count+=1  
                
        print(count)
                
        
for i in range(int(input())):
    a,b,c,d = map(int,input().split())
    t = ChefRaces(a,b,c,d)