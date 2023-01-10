# cook your dish here
tc = int(input())
for i in range(tc):
    a, b, x = map(int, input().split(" "))
    if (abs(a - b) / x) % 2 == 0 or a == b:
        print("YES")
    else:
        print("NO")