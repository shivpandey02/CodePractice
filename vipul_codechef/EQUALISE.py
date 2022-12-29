# cook your dish here
def make_equal(x,y):
    m,n = max(x,y),min(x,y)
    while (m>=n):
        if m == n:
            return 'YES'
        else:
            n*=2
    return 'NO'
        
                
for i in range(int(input())):
    a,b = map(int,input().split())
    print(make_equal(a,b))