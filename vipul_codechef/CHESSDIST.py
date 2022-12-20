# cook your dish here
def distance(a1,a2,b1,b2):
    a = abs(a1-b1)
    b = abs(a2-b2)
    return max(a,b)
    
for i in range(int(input())):
    a,b,c,d = map(int, input().split())
    print(distance(a,b,c,d))