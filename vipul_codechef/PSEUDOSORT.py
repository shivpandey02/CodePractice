# cook your dish here
def sorted_array(L,k):
    for i in range(k):
        a = min(L)
        index_number = L.index(a)
        if a == L[0]:
            L.remove(L[0])
            if L ==[]:
                return 'YES'
        elif a!=L[0]:
            L[0],L[index_number]=L[index_number],L[0]
            if L == sorted(L):
                return 'YES'
            return 'NO'
    
for i in range(int(input())):
    k = int(input())
    arr = [int(i) for i in input().split()]
    print(sorted_array(arr,k))
        