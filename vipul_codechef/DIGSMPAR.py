# cook your dish here
def sum_of_digit(number):
    digitsum = 0
    while number > 0:
        lastdigit=number%10
        digitsum+=lastdigit
        number//=10
    return digitsum 
    
def check_parity(number):
    k=sum_of_digit(number)
    if k%2 == 0:
        return 'Even' 
    return 'Odd'
        
def next_number(number):
    if check_parity(number) == 'Even':
        while True:
            number = number+1
            if check_parity(number) == 'Odd':
                return number 
    else:
        if check_parity(number) == 'Odd':
            while True:
                number+=1 
                if check_parity(number) == 'Even':
                    return number
def main():
    for i in range(int(input())):
        k = int(input())
        print(next_number(k))
        
main()
        
