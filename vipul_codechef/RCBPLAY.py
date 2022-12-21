# cook your dish here
def rcb(a,b,c):
    if (c*2 + a) >= b:
        return 'YES'
    else:
        return 'NO'
        
for i in range(int(input())):
    a,b,c = map(int, input().split())
    print(rcb(a,b,c))