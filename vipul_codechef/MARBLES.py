# cook your dish here
import math 
def marbles(n,k):
    return math.comb(n-1,k-1) 
    
for i in range(int(input())):
    n,k = map(int, input().split())
    print(marbles(n,k))