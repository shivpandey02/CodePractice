# cook your dish here
def validpair(a, b, c):
    if a==b or b==c or a == c:
        return 'YES'
    return 'No'



    
a,b,c = map(int,input().split())
print(validpair(a,b,c))