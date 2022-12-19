def arth(m,n):
    if (m+n)%2==0:
        return int((m+n)/2)
    else:
        return -1
        
l = int(input())
for i in range(l):
    k = [int(i) for i in input().split()]
    print(arth(k[0],k[1]))
    