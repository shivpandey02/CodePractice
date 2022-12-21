# cook your dish here
def prime_reversal(a, b):
    zero_a = a.count('1')
    zero_b = b.count('1')
    if zero_a == zero_b:
        return 'YES'
    else:
        return 'NO'

for i in range(int(input())):
    k = int(input())
    a = input()
    b = input()
    print(prime_reversal(a, b))