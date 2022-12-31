# cook your dish here
def matters(n,x,y,a,b):
    petrol_km = x/a 
    diesel_km = y/b
    if petrol_km < diesel_km:
        return 'PETROL'
    elif diesel_km < petrol_km:
        return 'DIESEL'
    else:
        return 'ANY'
        
for i in range(int(input())):
    n,x,y,a,b = map(int,input().split())
    print(matters(n,x,y,a,b))
    
