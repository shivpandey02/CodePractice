# cook your dish here
def his_student(pattern):
    count = 0
    n = len(pattern)
    for i in range(n-1):
        if pattern[i:i+2] == '<>':
            count+=1
    return count 
    
for i in range(int(input())):
    print(his_student(input()))
        
