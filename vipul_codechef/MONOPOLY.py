# cook your dish here
def monopoly_in_chefland(x,y,z):
    if x+y >= z:
        print('No')
    else:
        print('Yes')
        
for i in range(int(input())):
    x = [int(i) for i in input().split()]
    x.sort()
    monopoly_in_chefland(x[0],x[1],x[2])