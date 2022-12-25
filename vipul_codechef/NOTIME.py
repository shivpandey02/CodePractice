# cook your dish here
n,a,b1=map(int,input().split())
b=list(map(int,input().split()))
c=[]
for i in b:
    c.append(i+b1)
d=0
for i in c:
    if(i>=a):
        d+=1
if(d>=1):
    print("YES")
else:
    print("NO")