# cook your dish here
def delay(x,y):
    if y-x>5:
        return 1 
    else:
        return 0 
        
for i in range(int(input())):
    sumt = 0
    for i in range(int(input())):
        a,b = map(int,input().split())
        sumt+=delay(a,b)
    print(sumt)
        