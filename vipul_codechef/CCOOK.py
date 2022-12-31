# cook your dish here
def cookoff(l):
    s = sum(l)
    if s == 0:
        return 'Beginner'
    elif s == 1:
        return 'Junior Developer'
    elif s == 2:
        return 'Middle Developer'
    elif s == 3:
        return 'Senior Developer'
    elif s == 4:
        return 'Hacker'
    elif s == 5:
        return 'Jeff Dean'
        
for i in range(int(input())):
    l = [int(i) for i in input().split()]
    print(cookoff(l))