# cook your dish here
def pair(n,l,x):
    lst = [l]
    r = n-l 
    lst.append(r)
    pairs = min(lst)
    return pairs * x
    
        
for i in range(int(input())):
    a,b,c = map(int,input().split())
    print(pair(a,b,c))