# cook your dish here
def secret_recipe(x1,x2,x3,v1,v2):
    x3_to_x2 = abs(x3-x2)
    x3_to_x1 = abs(x3-x1)
    if x3_to_x1/v1 > x3_to_x2/v2:
        return 'Kefa'
    elif x3_to_x1/v1 == x3_to_x2/v2:
        return 'Draw'
    else:
        return 'Chef'
        
for i in range(int(input())):
    a,b,c,d,e = map(int,input().split())
    print(secret_recipe(a,b,c,d,e))