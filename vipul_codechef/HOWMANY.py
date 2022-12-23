# cook your dish here
def digits(number):
    length = len(number)
    if length == 1:
        return '1'
    elif length == 2:
        return '2'
    elif length == 3:
        return '3'
    else:
        return 'More than 3 digits'
    
print(digits(input()))