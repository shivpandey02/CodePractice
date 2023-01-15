# cook your dish here
# cook your dish here
def permutation(number):
    arr = list(range(1,number+1))
    new_arr = []
    if number%2==0:
        for i in range(number,0,-2):
            new_arr.append(i)
        for j in range(1,number,2):
            new_arr.append(j)
    else:
        for i in range(number,0,-2):
            new_arr.append(i)
        for j in range(2,number,2):
            new_arr.append(j)
            
    return new_arr
        
    
    
    
    
    
    
    
for i in range(int(input())):
    k = permutation(int(input()))
    print(*k)