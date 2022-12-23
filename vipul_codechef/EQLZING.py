# cook your dish here
def number(x,y):
    d = abs(x- y)
     # Check if the difference is a multiple of d
    if d%2 == 0:
        return 'Yes'
    else:
        return 'No'
        
for i in range(int(input())):
    x,y = map(int, input().split())
    print(number(x,y))