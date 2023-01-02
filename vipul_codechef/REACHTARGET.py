# cook your dish here
def target(x,y):
    b = y-x
    return abs(b) 
    
for i in range(int(input())):
    x,y = input().split()
    print(target(int(x),int(y)))