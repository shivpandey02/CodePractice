# cook your dish here
def maximum(a,b):
    return a//b 
    
for i in range(int(input())):
    a,b = map(int,input().split())
    print(maximum(a,b))