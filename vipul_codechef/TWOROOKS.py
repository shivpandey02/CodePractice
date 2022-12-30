# cook your dish here
def tworook(a,b,c,d):
    if a == c or b == d:
        return 'yes'
    return 'no'
    
for i in range(int(input())):
    a,b,c,d = map(int,input().split())
    print(tworook(a,b,c,d))