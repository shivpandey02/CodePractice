# cook your dish here
def utkarsh_and_placement_tests(perferencelist,offer):
    for i in perferencelist:
        for j in offer:
            if i == j:
                return i 
                
for i in range(int(input())):
    perferencelist = list(input().split())
    offer = list(input().split())
    print(utkarsh_and_placement_tests(perferencelist,offer))