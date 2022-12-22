# cook your dish here
import math
def nearest_court(x,y):
    difference = abs(x-y)
    return math.ceil(difference/2)
    
for i in range(int(input())):
    x,y = map(int, input().split())
    print(nearest_court(x,y))