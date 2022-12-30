# cook your dish here
def please(number):
    l=[]
    for i in range(1,number+1):
        l.append(i)
    list(l)
    return l  
    
for i in range(int(input())):
    k=please(int(input()))
    print(*k)
        