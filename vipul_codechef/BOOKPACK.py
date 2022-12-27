# cook your dish here
import math
def packing(x,y,z):
    selves = math.ceil(y/z)
    return x*selves
    
for i in range(int(input())):
    a,b,c = map(int,input().split())
    print(packing(a,b,c))