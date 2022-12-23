# cook your dish here
def count_zeroes(n):
    count = 0
    while n > 0:
        n = n // 5
        count += n
    return count
    
for i in range(int(input())):
    print(count_zeroes(int(input())))