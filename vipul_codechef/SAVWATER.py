# cook your dish here
import math
def save_water(H,x,y,C):
    gray_water = math.floor(y/2)
    water_need = x+gray_water
    total_need_in_chefland = water_need * H 
    if total_need_in_chefland <= C:
        return 'YES'
    return 'NO'
        
for i in range(int(input())):
    a,b,c,d = map(int, input().split())
    print(save_water(a,b,c,d))