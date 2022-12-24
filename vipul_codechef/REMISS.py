# cook your dish here
def remisses(x):
    maximum = max(x)
    print(maximum)
    print(sum(x))
    
for i in range(int(input())):
    x = [int(i) for i in input().split()]
    remisses(x)