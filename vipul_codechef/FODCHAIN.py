# cook your dish here
def food_chain(e,k):
    count = 1
    if k>e:
        return 1 
    else:
        while True:
            intail = e//k 
            if intail == 0:
                return count 
            count+=1 
            e=e//k
            
    
for i in range(int(input())):
    a,b = map(int,input().split())
    print(food_chain(a,b))