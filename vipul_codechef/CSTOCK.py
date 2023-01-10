# cook your dish here
def can_buy_stock(s, a, b, c):
    final_price = s * (1 + c / 100)  # calculate the final price based on the percentage change
    if a <= final_price <= b:  # check if the final price is within the acceptable range
        return 'yes'
    return 'no'

    
for i in range(int(input())):
    s,a,b,c = map(int,input().split())
    print(can_buy_stock(s,a,b,c))

