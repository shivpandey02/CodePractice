# cook your dish here
def insurance(x,y):
    if x >= y:
        return y
    else:
        return x 

n = int(input())
for i in range(n):
    x,y = map(int,input().split())

    print(insurance(x,y))