# cook your dish here
def area_or_perimater(l,b):
    area = l*b 
    peri = 2*(l+b)
    if area > peri:
        print('Area')
        print(area)
    elif peri >area:
        print('Peri')
        print(peri)
    
    else:
        print('Eq')
        print(area)
        
l = int(input())
b = int(input())
area_or_perimater(l,b)