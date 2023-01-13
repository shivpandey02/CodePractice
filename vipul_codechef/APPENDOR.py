def append_or(arr,y):
    need = 0
    for i in arr:
        need|=i
    if need|y == y:
        return y- need
    return -1
        



for i in range(int(input())):
    x,y = map(int,input().split())
    arr = [int(i) for i in input().split()]
    print(append_or(arr,int(y)))
