# cook your dish here
def chefland_visa(x1,x2,y1,y2,z1,z2):
    if x2>=x1 and y2>=y1 and z1>=z2:
        return 'YES'
    return 'NO'
    
for i in range(int(input())):
    x1,x2,y1,y2,z1,z2 = map(int,input().split())
    print(chefland_visa(x1,x2,y1,y2,z1,z2))
    