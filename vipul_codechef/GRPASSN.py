def assignment(number, arr):
    original_data = list(set(arr))
    for i in original_data:
        k = arr.count(i)
        if k%i!=0:
            return 'NO'
    return 'YES'

    
for i in range(int(input())):
    number = int(input())
    arr = [int(i) for i in input().split()]
    print(assignment(number,arr))
    
    
    
    