# cook your dish here
def power(arr1,arr2,l,r):
    result = 0
    for i in range(l-1,r):
        s = arr1[i]*arr2[i]
        result+=s 
    return result 
    
p,q = map(int,input().split())
arr1 = [int(i) for i in input().split()]
arr2 = [int(i) for i in input().split()]
for i in range(q):
    l,r = map(int,input().split())
    print(power(arr1,arr2,l,r))
        
        
    