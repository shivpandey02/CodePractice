# cook your dish here
def non_negative_product(l):
    product = 1 
    for i in l:
        product*=i
    if product >= 0:
        return 0
    else:
        return 1
        
    
for i in range(int(input())):
     k = int(input())
     l = map(int,input().split())
     print(non_negative_product(l))
            