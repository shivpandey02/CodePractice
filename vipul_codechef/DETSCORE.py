# cook your dish here
def determine_the_score(a,b):
    m = a//10
    return m*b 
    
for i in range(int(input())):
    a,b = map(int, input().split())
    print(determine_the_score(a,b))