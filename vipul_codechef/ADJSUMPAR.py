# cook your dish here
def sum_parity(l):
    s = sum(l)
    if s%2 == 0:
        return 'YES'
    return 'NO'

for i in range(int(input())):
    k = int(input())
    l = [int(i) for i in input().split()]
    print(sum_parity(l))
