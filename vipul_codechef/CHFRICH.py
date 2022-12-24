# cook your dish here
def richie_rich(current,goal,increment):
    count = 0
    while(current < goal):
        count+=1 
        current +=increment 
    return count 
    
for i in range(int(input())):
    x,y,z = map(int, input().split())
    print(richie_rich(x,y,z))