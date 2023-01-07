# cook your dish here
def sorted_array(arr,n):
    count = 0
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
            break 
    if arr == sorted(arr):
        return 'YES'
    return 'NO'
        
            #if count>1:
                #return 'NO'
    #return 'YES'
    
for i in range(int(input())):
    k = int(input())
    arr = [int(i) for i in input().split()]
    print(sorted_array(arr,k))
        