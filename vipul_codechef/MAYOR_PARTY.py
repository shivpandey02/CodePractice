# cook your dish here
def party(r1,r2,r3):
    if r1 + r3 > r2:
        return r1+r3
    else:
        return r2
        
for i in range(int(input())):
    r1,r2,r3 = map(int,input().split())
    print(party(r1,r2,r3))