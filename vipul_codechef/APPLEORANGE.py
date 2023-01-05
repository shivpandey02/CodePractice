# cook your dish here
import math
def apple_and_orange(apple,orange):
    return math.gcd(apple,orange)
    
        
for i in range(int(input())):
    a,b = map(int,input().split())
    print(apple_and_orange(a,b))
    
       
        
            
            
            
            
    