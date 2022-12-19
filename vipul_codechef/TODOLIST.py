# cook your dish here
def problem_in_your_list(x,y):
    count = 0
    for i in x:
        if i>=1000:
            count+=1 
    return count
    
for i in range(int(input())):
    n = int(input())
    y = [int(i) for i in input().split()]
    print(problem_in_your_list(y,n))