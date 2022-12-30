# cook your dish here
def cyberverse(n,k):
    return k//n
        
for i in range(int(input())):
    a,b = map(int,input().split())
    print(cyberverse(a,b))
        
    
    
