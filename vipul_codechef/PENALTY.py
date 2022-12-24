# cook your dish here
def penality(goals):
    l = len(goals)
    team_a = 0
    team_b = 0
    for i in range(1,l+1):
        if i%2 == 0:
            team_b+=goals[i-1] 
        else:
            team_a+=goals[i-1]
    if team_a > team_b:
        return '1'
    elif team_b > team_a:
        return '2' 
    else:
        return '0'
        
for i in range(int(input())):
    t = tuple(int(i) for i in input().split())
    print(penality(t))