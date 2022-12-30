# cook your dish here
def sumt(d,n):
    s=0 
    t=n 
    for i in range(d):
        s=0
        for i in range(1,t+1):
            s+=i 
        t=s 
    return s

        
for i in range(int(input())):
    a,b = map(int,input().split())
    print(sumt(a,b))
