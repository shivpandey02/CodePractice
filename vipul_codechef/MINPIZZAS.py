import math
def pizza(n,k):
    gcd = math.gcd(n,k)
    z =  n*k//gcd 
    return z//k
    
for i in range(int(input())):
    n,k = map(int,input().split())
    print(pizza(n,k))
    
    
    