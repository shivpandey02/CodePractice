# cook your dish here
def the_preparation(m,n,k):
    if m > n*k:
        return 'Yes'
    else:
        return 'No'
        
for i in range(int(input())):
    m,n,k = map(int, input().split())
    print(the_preparation(m,n,k))