# cook your dish here
def airline(a,b,c,d,e):
    if (a+b<=d) and(c<=e):
        return 'Yes'
    elif a+c<=d and b<=e:
        return 'Yes'
    elif b+c<=d and a<=e:
        return 'Yes'
    return 'No'
    
for i in range(int(input())):
    a,b,c,d,e = map(int,input().split())
    print(airline(a,b,c,d,e))
