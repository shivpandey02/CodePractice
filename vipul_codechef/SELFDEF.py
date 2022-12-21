# cook your dish here
def self_defence_training(l):
    count = 0
    for i in l:
        if i>=10 and i<=60:
            count+=1 
    return count
            
        
n = int(input())

for i in range(n):
    a = int(input())
    l = [int(i) for i in input().split()]
    print(self_defence_training(l))