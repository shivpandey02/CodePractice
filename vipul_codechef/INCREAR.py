# cook your dish here
def equal_integer(x,y):
    if x==y:
        return 0 
    elif x<y:
            return y-x 
    else:
        d = abs(y-x)
        if d%2==0:
            return int(d/2) 
        return int(d/2)+2
        
for i in range(int(input())):
    a,b = map(int,input().split())
    print(equal_integer(a,b))
            