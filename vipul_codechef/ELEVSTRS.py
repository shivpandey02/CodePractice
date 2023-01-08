# cook your dish here
def speed(n,v1,v2):
    lift_time = (2*n)/v2 
    stair_time = (((2)**0.5)*n)/v1 
    if lift_time > stair_time:
        return 'Stairs'
    return 'Elevator'
    
for i in range(int(input())):
    a,v1,v2 = map(int,input().split())
    print(speed(a,v1,v2))
    