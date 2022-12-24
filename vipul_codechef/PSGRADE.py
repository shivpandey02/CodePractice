# cook your dish here
def marks(am,bm,cm,tm,a,b,c):
    total = a + b + c 
    if am<=a and bm<=b and cm<=c and total >= tm:
        return 'Yes'
    return 'No'
    
for i in range(int(input())):
    am,bm,cm,tm,a,b,c = map(int,input().split())
    print(marks(am,bm,cm,tm,a,b,c))