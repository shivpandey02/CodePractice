# cook your dish here
def multiple(number):
    l = [0,5]
    for i in number:
        if i in l:
            return 'YES'
    return 'NO'

for i in range(int(input())):
    k = int(input())
    number = [int(i) for i in input()]
    print(multiple(number))