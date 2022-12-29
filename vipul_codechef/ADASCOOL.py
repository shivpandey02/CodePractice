# cook your dish here
def ada_school(n,m):
    num = n * m
    if num % 2 == 0:
        return 'YES'
    return 'NO'


    
for i in range(int(input())):
    a,b = map(int, input().split())
    print(ada_school(a,b))