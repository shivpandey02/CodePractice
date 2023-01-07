# cook your dish here
def lost_weekened(work):
    p = work.pop()
    work = [i*p for i in work]
    s = sum(work)
    number_of_hour_in_5_days = 24*5 
    number_of_hour_left = number_of_hour_in_5_days - s 
    if number_of_hour_left < 0 :
        return 'Yes'
    return 'No'
    
for i in range(int(input())):
    lst = [int(i) for i in input().split()]
    print(lost_weekened(lst))
