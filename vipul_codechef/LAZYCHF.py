# cook your dish here
def lazychef(x,m,d):
    m = x*m 
    n = x+d 
    l = [m,n]
    return min(l)
    
for i in range(int(input())):
    a,b,c = map(int,input().split())
    print(lazychef(a,b,c))
