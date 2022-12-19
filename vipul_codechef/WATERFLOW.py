# cook your dish here
def bucket(w,x,y,z):
    water = y*z 
    if x == w + water:
        return 'filled'
    elif x < w+water:
        return 'overflow'
    else:
        return 'Unfilled'
        
for i in range(int(input())):
    w,x,y,z = map(int, input().split())
    print(bucket(w,x,y,z))