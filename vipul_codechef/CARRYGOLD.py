# cook your dish here
def gold_mining(n,x,y):
    if n*y >= x:
        return 'YES'
    else:
        return 'NO'
        
for i in range(int(input())):
    a,b,c = map(int,input().split())
    print(gold_mining(a+1,b,c))