# cook your dish here
# cook your dish here
def makeitdivisible(number):
    digit_number = 1
    for i in range(number):
        digit_number*=10 
    starting_number = digit_number//10
    
    for i in range(starting_number,digit_number):
        if i%2!=0 and i%3==0 and i%9!=0:
            return i  
            
n = int(input())
for i in range(n):
    print(makeitdivisible(int(input())))
    

            
        
        