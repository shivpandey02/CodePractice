# cook your dish here
def car_choice(x1,x2,y1,y2):
    car1 = x1/y1
    car2 = x2/y2 
    if car1 > car2:
        return '-1'
    elif car2 > car1:
        return '1'
    else:
        return '0'
        
for i in range(int(input())):
    a,b,c,d = map(int, input().split())
    print(car_choice(a,b,c,d))