# cook your dish here
def find_degree(coefficient):
    #iterate through the coefficient
    for i in range(len(coefficient)-1,-1,-1):
        if coefficient[i]!=0:
            return i 
n = int(input())
for i in range(n):
    k = int(input())
    j = tuple(int(i) for i in input().split())
    print(find_degree(j))
    
            