# cook your dish here
def eat(n,k):
    if n%k==0:
        return int(n/k)
    return -1
    
for i in range(int(input())):
    n,k = map(int,input().split())
    print(eat(n,k))