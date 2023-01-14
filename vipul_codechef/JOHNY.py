# cook your dish here
def uncle_jonny(arr,k):
    s = arr[k-1]
    arr.sort()
    for i in range(len(arr)):
        if arr[i] == s:
            return i+1
         
for i in range(int(input())):
    length = int(input())
    arr = [int(i) for i in input().split()]
    k = int(input())
    print(uncle_jonny(arr,k))
