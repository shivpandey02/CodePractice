# cook your dish here
def drunk_alcohol(x):
    step = 0
    for i in range(1,x+1):
        if i%2==0:
            step-=1 
        else:
            step+=3 
    return step 
    
for i in range(int(input())):
    print(drunk_alcohol(int(input())))
            