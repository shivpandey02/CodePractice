# cook your dish here
#I write this code only for pratice by class 
class FindingShoes:
    def __init__(self,shoes,friend):
        self.shoes = shoes
        self.friend = friend
        print(self.pair())
        
    def pair(self):
        if self.shoes >= self.friend:
            return self.friend
        else:
            left = self.friend - self.shoes  
            return left + self.friend
for i in range(int(input())):           
    friend,shoes = map(int,input().split())
    s = FindingShoes(shoes,friend)
