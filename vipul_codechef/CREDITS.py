# cook your dish here
def complete_the_credit(credits):
    if credits > 65:
        return 'Overload'
    elif credits < 35:
        return 'Underload'
    else:
        return 'Normal'
        
for i in range(int(input())):
    print(complete_the_credit(int(input())))