# cook your dish here
def games(l):
    s = sum(l)
    if s%2==0:
        return 'Janmansh'
    return 'Jay'

for i in range(int(input())):
    l = [int(i) for i in input().split()]
    print(games(l))