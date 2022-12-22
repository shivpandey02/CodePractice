# cook your dish here
def cars_and_bikes(no_of_tyres):
    if no_of_tyres%4 >= 2:
        return 'YES'
    elif no_of_tyres%4 == 0:
        return 'NO'
        
for i in range(int(input())):
    print(cars_and_bikes(int(input())))
        