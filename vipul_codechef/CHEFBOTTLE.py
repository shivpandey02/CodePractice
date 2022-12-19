# cook your dish here
def water_bottle(a,b,c):
    count = 0
    for i in range(1,a+1,1):
        if i*b <= c:
            count+=1 
    return count
for i in range(int(input())):
    a,b,c = map(int, input().split())
    print(water_bottle(a,b,c))
        