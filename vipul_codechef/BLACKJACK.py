# cook your dish here
class BlackJack:
    def __init__(self,a,b):
        self.a = a  
        self.b = b 
        self.yes_or_no()
    
    def yes_or_no(self):
        sum = self.a + self.b 
        number = 21 - sum 
        if 1<=number<=10:
            print(number) 
        else:
            print(-1) 
            
for i in range(int(input())):
    a,b = map(int,input().split())
    t = BlackJack(a,b)
