# cook your dish here
def increment_decrement(number):
    if number%4==0:
        return number+1 
    else:
        return number - 1 

print(increment_decrement(int(input())))