# cook your dish here
def snapchat(chef,chefina,k):
    count = 0
    maximum = 0
    for i in range(k):
        if chef[i]!=0 and chefina[i]!=0:
            count+=1 
            if maximum < count:
                maximum = count 
        else:
            count = 0
    return maximum 
    
for i in range(int(input())):
    k = int(input())
    chef = [int(i) for i in input().split()]
    chefina = [int(i) for i in input().split()]
    print(snapchat(chef,chefina,k))
        