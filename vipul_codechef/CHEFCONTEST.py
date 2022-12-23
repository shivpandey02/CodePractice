# cook your dish here
def chef_and_contest(x,y,p,q):
    if (x) + (p*10) < (y) + (q*10):
        print('Chef')
    elif (x) + (p*10) == (y) + (q*10):
        print('Draw')
    else:
        print('Chefina')
        
for i in range(int(input())):
    x,y,p,q = map(int, input().split())
    chef_and_contest(x,y,p,q)