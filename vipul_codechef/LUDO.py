# cook your dish here
def token(number):
    if number%6==0:
        return 'YES'
    return 'NO'
    
for i in range(int(input())):
    print(token(int(input())))