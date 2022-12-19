# cook your dish here
def thethreetopics(a,b,c,x):
    if a==x or b==x or c == x:
        return 'Yes'
    else:
        return 'No'
        
a,b,c,d = map(int, input().split())
print(thethreetopics(a,b,c,d))