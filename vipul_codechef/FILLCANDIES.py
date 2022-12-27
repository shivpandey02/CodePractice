# cook your dish here
import math
class FillCandies:
    def __init__(self,n,k,m):
        self.n = n 
        self.k = k 
        self.m = m
        print(self.number_of_bag())
        
    def number_of_bag(self):
        candies_in_one_bag = self.k * self.m 
        need_of_bag = self.n/candies_in_one_bag
        return math.ceil(need_of_bag)
        
for i in range(int(input())):
    a,b,c = map(int,input().split())
    t = FillCandies(a,b,c)