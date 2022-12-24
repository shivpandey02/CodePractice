# cook your dish here
def find_the_direction(number):
    degree = 90
    for i in range(1,number+1):
        if degree == 360:
            degree = 0
        degree+=90
        
    if degree == 90:
        return 'North'
    elif degree == 180:
        return 'East'
    elif degree == 270:
        return 'South'
    elif degree == 360:
        return 'West'
        
for i in range(int(input())):
    print(find_the_direction(int(input())))
        