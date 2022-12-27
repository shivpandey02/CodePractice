# cook your dish here
#I write this code in oops just practice
class BlackChessboard:
    
    def __init__(self,n):
        self.n = n   
        self.even_cell()
        
    
    def even_cell(self):
        total_cell = self.n * self.n 
        print(int(total_cell/2))
        
BlackChessboard(int(input()))