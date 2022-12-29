# cook your dish here
def economics(l1,l2):
    count = 0 
    for i in range(k):
        if l1[i] is l2[i]:
            count+=1 
    return count
            
    
for i in range(int(input())):
    k = int(input())
    l1 = [int(i) for i in input().split()]
    l2 = [int(i) for i in input().split()]
    print(economics(l1,l2))
    
