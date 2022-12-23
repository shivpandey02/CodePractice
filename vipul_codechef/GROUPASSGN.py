# cook your dish here
for _ in range(int(input())):
    n,x=map(int,input().split())
    if x==n:
        print(n+1)
    elif x<n:
        print(n+(n-x)+1)
    else:
        print(n-(x-n)+1)
        
    