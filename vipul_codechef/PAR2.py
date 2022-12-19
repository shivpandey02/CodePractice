def choco(number):
    if number%2==0:
        return 'Yes'
    else:
        return 'No'
        
n =int(input())
for i in range(n):
    c = int(input())
    print(choco(c))
    
