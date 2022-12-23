# cook your dish here
def chef_and_profit(x,y,z):
    amount_spend = x * y
    total_amount = x * z 
    return total_amount - amount_spend 

for i in range(int(input())):
    a,b,c = map(int, input().split())
    print(chef_and_profit(a,b,c))