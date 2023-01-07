# cook your dish here
def problem(lst,n):
    for i in lst:
        if i%2!=0:
            lst.remove(i)
            break 
    s = sum(lst)
    if s%2==0:
        return 'NO'
    return 'YES'
    
for i in range(int(input())):
    k = int(input())
    lst = [int(i) for i in input().split()]
    print(problem(lst,k))            
