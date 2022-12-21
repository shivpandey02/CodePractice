# cook your dish here
def is_drinking_water(water_litre):
    if water_litre >= 2000:
        return 'YES'
    return 'NO'
    
for i in range(int(input())):
    print(is_drinking_water(int(input())))