# cook your dish here
def mask_policy(a,b):
    c = a-b
    k = min(b,c)
    return k 
    
for i in range(int(input())):
    a,b = map(int,input().split())
    print(mask_policy(a,b))
