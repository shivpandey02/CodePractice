# cook your dish here
def manipulate(x,y):
    if x >= y:
        return 'YES'
    else:
        return 'NO'
        
number_of_input = int(input())
for i in range(number_of_input):
    x,y = map(int,input().split())
    print(manipulate(x,y))
