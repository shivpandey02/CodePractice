# cook your dish here
import math
def prime(number):
    if number < 2:
        return 'no'
    for i in range(2,number):
        if number%i==0:
            return 'no'
    return 'yes'
        
       
for i in range(int(input())):
    print(prime(int(input())))