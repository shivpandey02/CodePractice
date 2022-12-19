# cook your dish here
def miami(x,y):
    if x*1.07 >= y:
        return 'Yes'
    else:
        return 'No'
        
for i in range(int(input())):
    x,y = map(int, input().split())
    print(miami(x,y))