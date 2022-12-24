# cook your dish here
def count_the_holiday(holiday,k):
    sat_sun = []
    sat = 6 
    sun = 7
    for i in range(1,31):
        if i%sat == 0:
            sat_sun.append(sat)
            sat+=7
        if i%sun == 0:
            sat_sun.append(sun)
            sun+=7 
    count =len(sat_sun)
    for i in range(k):
        if holiday[i] not in sat_sun:
            count+=1 
    return count   
    
            
            
    
for i in range(int(input())):
    k = int(input())
    b = tuple(int(i) for i in input().split())
    print(count_the_holiday(b,k))