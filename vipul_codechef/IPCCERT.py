# cook your dish here
def certificate(time,m):
    summ = sum(time[0:-1])
    last_digit = time[-1]
    if summ >= m and last_digit <= 10:
        return 1
    else:
        return 0
        

n,m,k = map(int,input().split())
count = 0 
for i in range(n):
    time = tuple(int(i) for i in input().split())
    
    function_call = certificate(time,m)
    count+=function_call 
print(count)