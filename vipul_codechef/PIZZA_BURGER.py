# cook your dish here
def choose(x,y,z):
    if x >=y:
        return 'PIZZA'
    elif x >=z:
        return 'BURGER'
    else:
        return 'NOTHING'
        
for i in range(int(input())):
    x,y,z = map(int,input().split())
    print(choose(x,y,z))