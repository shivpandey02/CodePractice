# cook your dish here
def score_high(a,b,c,d):
    return max(a,b,c,d)
    
for i in range(int(input())):
    k = int(input())
    a,b,c,d = map(int,input().split())
    print(score_high(a,b,c,d))