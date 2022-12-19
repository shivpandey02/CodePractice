# cook your dish here
def throw(a,b,c):
    return max(a,b,c)
    
for i in range(int(input())):
    a,b,c = map(int,input().split())
    print(throw(a,b,c))