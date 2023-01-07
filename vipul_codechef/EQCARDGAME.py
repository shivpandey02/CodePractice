# cook your dish here
def equal_card(number):
    if 52%number==0:
        return 0 
    return 52%number
    
for i in range(int(input())):
    print(equal_card(int(input())))
        