# cook your dish here
def relation(a,b):
    if a>b:
        print('>')
    elif a<b:
        print('<')
    elif a == b:
        print('=')
        
for i in range(int(input())):
    a,b = map(int,input().split())
    relation(a,b)
