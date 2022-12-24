# cook your dish here
def chef_on_vacation(x,y,z):
    if x+y <= z:
        print('YES')
    else:
        print('NO')

for i in range(int(input())):
    x,y,z = map(int, input().split())
    chef_on_vacation(x,y,z)