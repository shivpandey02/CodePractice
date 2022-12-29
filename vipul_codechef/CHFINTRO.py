# cook your dish here
def contest(m,n):
    if n<=m:
        return 'Good boi'
    return 'Bad boi'
    
a,b = map(int,input().split())
for i in range(a):
    m = int(input())
    print(contest(m,b))