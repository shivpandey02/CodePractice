# cook your dish here
def sum_it(a,b,c):
    if a+b == c:
        return 'YES'
    return 'NO'
    
for i in range(int(input())):
    a,b,c = map(int,input().split())
    print(sum_it(a,b,c))
