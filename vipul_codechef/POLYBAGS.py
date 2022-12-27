# cook your dish here
# I write this code for oop practice
import math 
class TooManyItem:
    
    def __init__(self,item):
        self.item = item 
        self.number()
        
    def number(self):
        print(math.ceil(self.item/10))
        
for i in range(int(input())):
    t = TooManyItem(int(input()))
