# cook your dish here
def shoes_fit(a):
    z = a.count('0')
    o = a.count('1')
    if z == 2 and o == 1 or o==2 and z==1:
        return '1'
    return '0'
    
for i in range(int(input())):
    a = tuple(input().split())
    print(shoes_fit(a))
