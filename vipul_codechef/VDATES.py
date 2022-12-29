# cook your dish here
def vaccine_days(d,l,r):
    if l<=d<=r:
        return 'Take second dose now'
    elif d>l and d>r:
        return 'Too Late'
    elif d<r and d<r:
        return 'Too Early'
        
        
for i in range(int(input())):
    a,b,c = map(int,input().split())
    print(vaccine_days(a,b,c))