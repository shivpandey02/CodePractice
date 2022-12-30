# cook your dish here
def grid(n,m):
    if n%2==0:
        if m%2==0:
            print(0)
        else:
            print(n)
    else:
        if m%2==0:
            print(m)
        else:
            print(m+n-1)
            
for i in range(int(input())):
    n,m = map(int,input().split())
    grid(n,m)
