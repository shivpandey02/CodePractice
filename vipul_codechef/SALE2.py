# cook your dish here
import math
def buy_get(x,y):
    count = 0
    for i in range(1,x+1):
        if i%3 != 0:
            count+=y 
    return count
            
            
    
for i in range(int(input())):
    x,y = map(int,input().split())
    print(buy_get(x,y))
    