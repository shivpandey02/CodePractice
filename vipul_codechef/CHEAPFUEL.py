# cook your dish here
def cheaper_fuel(x,y,a,b,k):
    petrol = x 
    diesel = y 
    for i in range(k):
        petrol +=a 
        diesel +=b 
        
    if petrol < diesel:
        return 'PETROL'
    elif diesel < petrol:
        return 'DIESEL' 
    else:
        return 'SAME PRICE'
        
for i in range(int(input())):
    x,y,a,b,k = map(int,input().split())
    print(cheaper_fuel(x,y,a,b,k))
        
    