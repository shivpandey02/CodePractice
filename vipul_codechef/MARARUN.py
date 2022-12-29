# cook your dish here
def marathon(D,d,A,B,C):
    km = D*d 
    if 10<= km < 21:
        return A  
    elif 21<= km <42:
        return B  
    elif 42 <= km:
        return C  
    else:
        return 0  
        
for i in range(int(input())):
    a,b,c,d,e = map(int,input().split())
    print(marathon(a,b,c,d,e))