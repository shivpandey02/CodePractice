# cook your dish here
def carchoice(a,b,c,d):
    car1 = c/a     
    car2 = d/b  
    if car1 < car2:
        return -1 
    elif car1 == car2:
        return '0'
    else:
        return '1'
        
for i in range(int(input())):
    a,b,c,d = map(int,input().split())
    print(carchoice(a,b,c,d))