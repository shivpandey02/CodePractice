# cook your dish here
def mixtuere(solid,liquid):
    if solid > 0 and liquid > 0:
        print('Solution')
    elif liquid == 0:
        print('Solid')
    elif solid == 0:
        print('Liquid')
        
for i in range(int(input())):
    a,b = map(int, input().split())
    mixtuere(a,b)