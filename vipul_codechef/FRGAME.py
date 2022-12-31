# cook your dish here
def game(a,b,c,d):
    if a<b:
        a+=c 
    else:
        b+=c 
    if a<b:
        a+=d 
    else:
        b+=d 
    if a>=b:
        return 'N'
    else:
        return 'S'
    
for i in range(int(input())):
    a,b,c,d = map(int,input().split())
    print(game(a,b,c,d))