# cook your dish here
def kitchen_timming(start,end):
    return end - start
    
for i in range(int(input())):
    start,end = map(int,input().split())
    print(kitchen_timming(start,end))