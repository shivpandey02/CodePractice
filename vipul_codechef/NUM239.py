# cook your dish here
def counting_pretty_number(x,y):
    count = 0
    while(x<=y):
        if x%10==2 or x%10==3 or x%10==9:
            count+=1 
        x+=1 
    return count
    
for i in range(int(input())):
    x,y = map(int,input().split())
    print(counting_pretty_number(x,y))
