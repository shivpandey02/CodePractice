def deal(m,n):
    if m-n>0:
        print("LOSS")
    elif m-n<0:
        print('PROFIT')
    else:
        print("NEUTRAL")
        
l = int(input())
for i in range(l):
    k = [int(i) for i in input().split()]
    deal(k[0],k[1])
