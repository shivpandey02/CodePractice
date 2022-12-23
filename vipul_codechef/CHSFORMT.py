# cook your dish here
def format(a,b):
    if a + b  < 3:
        print(1)
    elif a + b <= 10:
        print(2)
    elif  a + b <= 60:
        print(3)
    elif a+b > 60:
        print(4)
        
for i in range(int(input())):
    a,b = map(int, input().split())
    format(a,b)
