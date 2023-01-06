# cook your dish here

for i in range(int(input())):
    l,r = map(int,input().split())
    highest = r + r
    lowest = l + l
    ans = highest - lowest + 1
    print(ans)
