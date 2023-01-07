# cook your dish here
def changeit(lst,n):
    count = 0 
    for i in range(n):
        k = lst.count(lst[i])
        if count < k:
            count = k 
    return n-count 
    
for i in range(int(input())):
    k = int(input())
    lst = [int(i) for i in input().split()]
    print(changeit(lst,k))
