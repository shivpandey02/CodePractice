# cook your dish here
def three_question(l1,l2):
    l1.sort()
    l2.sort()
    if l1 == l2:
        return 'Pass'
    return 'Fail'

for i in range(int(input())):
    l1 = [int(i) for i in input().split()]
    l2 = [int(i) for i in input().split()]
    print(three_question(l1,l2))