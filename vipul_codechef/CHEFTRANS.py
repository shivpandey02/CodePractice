# cook your dish here
def chef_trnasport(x,y,z):
    route1 = x+y   
    route2 = z   
    if route1<route2:
        return 'PLANEBUS'
    elif route1 == route2:
        return 'EQUAL'
    else:
        return 'TRAIN'
        
for i in range(int(input())):
    a,b,c = map(int,input().split())
    print(chef_trnasport(a,b,c))