# cook your dish here
def devendra(z,y,a,b,c):
    amount_remaining = z - y     
    total_cost_of_water_sport = a+b+c 
    if amount_remaining >= total_cost_of_water_sport:
        return 'YES'
    return 'NO'
    
for i in range(int(input())):
    z,y,a,b,c = map(int,input().split())
    print(devendra(z,y,a,b,c))