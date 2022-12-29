# cook your dish here
def summer_heat(a,b,c,d):
    k = c//a
    j = d//b 
    return k+j 
    
for i in range(int(input())):
    a,b,c,d = map(int,input().split())
    print(summer_heat(a,b,c,d))