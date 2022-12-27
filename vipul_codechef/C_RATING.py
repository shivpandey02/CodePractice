# cook your dish here
#I write this code for to clear the concept of oops 
import math
class ChessRating:
    
    def __init__(self,a,b):
        self.a = a  
        self.b = b   
        self.minimum_game()
        
    def minimum_game(self):
        if self.a >= self.b:
            print(0)
        else:
            score_need = self.b - self.a
            no_game = math.ceil(score_need/8)
            print(no_game)
            
for i in range(int(input())):
    a,b = map(int,input().split())
    t = ChessRating(a,b)
            
            
        
    