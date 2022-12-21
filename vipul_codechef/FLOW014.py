# cook your dish here
def grade_the_steel(h,c,t):
    if h > 50 and c < 0.7 and t > 5600:
        return 10
    elif h > 50 and c < 0.7:
        return 9
    elif c < 0.7 and t > 5600:
        return 8 
    elif h > 50 and t > 5600:
        return 7 
    elif h > 50 or c < 0.7 or t > 5600:
        return 6 
    else:
        return 5 
        
for i in range(int(input())):
    a,b,c = map(float, input().split())
    print(grade_the_steel(a,b,c))