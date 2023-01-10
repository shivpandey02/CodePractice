# cook your dish here
def string(pattern,x,y,n):
    if pattern.count('0')==n or pattern.count('1')==n:
        return 0 
    else:
        return min(x,y)
for i in range(int(input())):
    n,x,y = map(int,input().split())
    st = input()
    print(string(st,x,y,n))
            