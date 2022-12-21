# cook your dish here
def cup_final(a,b,c):
    if abs(a-b)<=c:
        return 'Yes'
    else:
        return 'No'
        
for i in range(int(input())):
    a,b,c = map(int, input().split())
    print(cup_final(a,b,c))