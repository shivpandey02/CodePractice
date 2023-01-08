# cook your dish here
def candy_love(arr):
    s = sum(arr)
    if s%2==0:
        return 'NO'
    return 'YES'
    
for i in range(int(input())):
    K = int(input())
    arr = [int(i) for i in input().split()]
    print(candy_love(arr))