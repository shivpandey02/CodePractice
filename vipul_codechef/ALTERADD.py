# cook your dish here
def alternante_number(a,b):
    d=b-a
    if(d==0 or d==1 or d==3 or d%3==1 or d%3==0):
        print("Yes")
    else:
        print("no")
                
                
for i in range(int(input())):
    a,b = map(int,input().split())
    alternante_number(a,b)
        
            