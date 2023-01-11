# cook your dish here
def coins(number):
    row = 1 
    i = 1 
    count = 0
    while True:
        if number >= row:
            i+=1 
            row+=i
            count+=1 
        else:
            return count
            
for i in range(int(input())):
    print(coins(int(input())))
    
        
