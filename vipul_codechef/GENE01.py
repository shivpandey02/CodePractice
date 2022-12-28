# cook your dish here
def genes(x,y):
    if x == y:
        return x
    if x != y:
        if x == 'R' or y =='R':
            return 'R' 
        else:
            return 'B'
        

a,b = map(str,input().split())
print(genes(a,b))