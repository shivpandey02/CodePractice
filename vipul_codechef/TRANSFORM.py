# cook your dish here
#I write this code in the form of class just for practice 
class MarioAndTransformation:
    def __init__(self,state):
        self.state = state 
        for i in range(self.state):
            number = int(input())
            self.number = number 
            print(self.size())
            
    def size(self):
        current = self.number % 3 
        if current == 1:
            return 'huge'
        elif current == 2:
            return 'small'
        else:
            return 'normal'
            
l = int(input())
MarioAndTransformation(l)