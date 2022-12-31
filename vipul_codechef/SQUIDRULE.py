# cook your dish here
def game(l,k):
    minimum = min(l)
    s = sum(l)
    return s - minimum 
    
for i in range(int(input())):
    k = int(input())
    l = [int(i) for i in input().split()]
    print(game(l,k))