# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    v=['a','e','i','o','u']
    s=list(s)
    c=0
    max=0
    for i in s:
        if i not in v:
            c+=1
            if max<c:
                max=c
        else:
            c=0
    if max>=4:
        print("NO")
    else:
        print("YES")
            