# cook your dish here
def jump(x,y):
    if x<y:
        return x
    else:
        return (x//y) + (x-(x//y)*y)
    
for i in range(int(input())):
    a = [int(i) for i in input().split()]
    print(jump(a[0],a[1]))