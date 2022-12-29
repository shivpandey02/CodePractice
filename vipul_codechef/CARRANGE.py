# cook your dish here
def car_range(p,m,v):
    average_with_persons = m-p+1
    return average_with_persons*v 
    
for i in range(int(input())):
    p,m,v = map(int,input().split())
    print(car_range(p,m,v))
