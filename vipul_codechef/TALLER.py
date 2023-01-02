# cook your dish here
def taller(x,y):
    if x>y:
        return 'A'
    return 'B'
    
for i in range(int(input())):
    a,b = input().split()
    print(taller(int(a),int(b)))