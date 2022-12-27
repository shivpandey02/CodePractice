# cook your dish here
#I write this code for oop practice
class Count:
    
    def __init__(self,score):
        self.score = score 
        self.number()
    def number(self):
        hundred_marks = self.score//100
        one = self.score - hundred_marks*100 
        if hundred_marks + one > 10:
            print(-1)
        else:
            print(hundred_marks+one)
            
for i in range(int(input())):
    t = Count(int(input()))