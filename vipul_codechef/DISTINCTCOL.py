# cook your dish here
def distinct_color(l):
    maximum = max(l)
    return maximum
    
for i in range(int(input())):
    k = int(input())
    l = [int(i) for i in input().split()]
    print(distinct_color(l))