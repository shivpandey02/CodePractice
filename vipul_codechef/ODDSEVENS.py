# cook your dish here
def odd_even(x,y):
    sum = x+y  
    if sum%2==0:
        return 'Bob'
    return 'Alice'
    
for i in range(int(input())):
    a,b = map(int,input().split())
    print(odd_even(a,b))