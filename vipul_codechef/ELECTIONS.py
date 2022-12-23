# cook your dish here
def elections_in_chefland(A,B,C):
    if A > 50:
        return 'A' 
    elif B > 50:
        return 'B' 
    elif C > 50:
        return 'C' 
    else:
        return 'NOTA'
        
for i in range(int(input())):
    a,b,c = map(int, input().split())
    print(elections_in_chefland(a,b,c))

    