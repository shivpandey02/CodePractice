# cook your dish here
def candies(arr):
    for i in range(len(arr)):
        if arr.count(arr[i]) > 2:
            return 'NO'
    return 'YES'
    
    
for i in range(int(input())):
    k = int(input())
    arr = [int(i) for i in input().split()]
    print(candies(arr))