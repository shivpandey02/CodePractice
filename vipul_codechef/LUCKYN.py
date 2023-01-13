# cook your dish here
def lucky_number(number):
    if '7' in number:
        return 'YES'
    return 'NO'
    
for i in range(int(input())):
    print(lucky_number(input()))
