# cook your dish here
class PresentsForCheffina:
    
    def __init__(self,n_item):
        self.n_item = n_item  
        self.coin_required()
        
    def coin_required(self):
        number_of_free_item = self.n_item//5
        cost = self.n_item - number_of_free_item
        print(cost)
        
for i in range(int(input())):
    PresentsForCheffina(int(input()))