# cook your dish here
def instagram(x,y):
    time = x/y
    if time > 10:
        return 'yes'
    return 'No'
    
for i in range(int(input())):
    x,y = map(int,input().split())
    print(instagram(x,y))
