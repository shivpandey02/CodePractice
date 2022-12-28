# cook your dish here
def second_largest(number):
    number.sort(reverse = True)
    print(number[1])
    
for i in range(int(input())):
    l = [int(i) for i in input().split()]
    second_largest(l)