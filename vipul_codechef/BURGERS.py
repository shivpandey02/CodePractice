# cook your dish here
def number_of_burger(no_of_paties,no_of_buns):
    return min(no_of_paties,no_of_buns)
    
for i in range(int(input())):
    a,b = map(int,input().split())
    print(number_of_burger(a,b))