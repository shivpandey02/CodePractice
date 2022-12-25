# cook your dish here
def missing_clsses(days):
#    day = 6
#    count = 0
#    for i in range(1,days+1):
#        if i%day==0 :
#            count+=1 
#            day+=7
#    return count 
    a = days//7
    b = days%7 
    if b == 6:
        return a+1 
    else:
        return a
    
for i in range(int(input())):
    print(missing_clsses(int(input())))
            
