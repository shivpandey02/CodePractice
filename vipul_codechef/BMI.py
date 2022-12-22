# cook your dish here
def Body_mass_index(mass,height):
    bmi = mass/pow(height,2)
    if bmi <= 18:
        print(1)
    elif bmi <= 24:
        print(2)
    elif bmi <= 29:
        print(3)
    elif bmi >= 30:
        print(4)
        
for i in range(int(input())):
    a,b = map(int, input().split())
    Body_mass_index(a,b)