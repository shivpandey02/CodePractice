# cook your dish here
def atm_machine(amount,l):
    string = ''
    for i in l:
        if amount >= i:
            amount-=i 
            string+='1'
        else:
            string+='0'
            
    return string
    
for i in range(int(input())):
    c,m = map(int,input().split())
    l = [int(i) for i in input().split()]
    print(atm_machine(m,l))
            