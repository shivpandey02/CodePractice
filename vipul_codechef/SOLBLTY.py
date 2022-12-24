# cook your dish here
def solubility(a,b,c):
    v = 100 - a 
    k = v*c 
    l = b+k 
    return l*10

for i in range(int(input())):
    a,b,c = map(int,input().split())
    print(solubility(a,b,c))