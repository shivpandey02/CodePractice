# cook your dish here
def score(a,b):
    if a[0]<=b[0] and a[1]<=b[1]:
        return 'POSSIBLE'
    else:
        return 'IMPOSSIBLE'
        
for i in range(int(input())):
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    print(score(a,b))