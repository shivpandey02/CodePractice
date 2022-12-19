def reachfast(starting, ending, step):
    number_of_step = 0
    if ending < starting:
        starting,ending = ending, starting
    if starting - ending == 0:
        return 0
    elif ending - starting < step:
        return 1
    else:
        for i in range(starting,ending+1,step):
            number_of_step+=1 
            
        if ending > i:
            number_of_step+=1
        return number_of_step-1
        
n = int(input())
for i in range(n):
    a,b,c = map(int, input().split())
    print(reachfast(a,b,c))
        
