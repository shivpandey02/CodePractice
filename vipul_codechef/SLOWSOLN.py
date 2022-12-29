# cook your dish here
def slowsolution(a, b, c):
    test_case_sum = pow(b,2) 
    s = 2*b   
    t = 1
    while(t<a and s<c+1):
        test_case_sum += pow(b,2)
        t+=1 
        s+=b 
    
    if s-b == c  or t == a:
        return test_case_sum
    else:
        rem = c - (s-b)
        return pow(rem,2) + test_case_sum
        
        
            

    
for i in range(int(input())):
    a,b,c = map(int,input().split())
    print(slowsolution(a,b,c))