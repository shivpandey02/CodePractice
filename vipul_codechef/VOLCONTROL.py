# cook your dish here
def volume_control(x,y):
    return abs(x-y)

n = int(input())
for i in range(n):
    i = [int(i) for i in input().split()]
    print(volume_control(i[0],i[1]))
