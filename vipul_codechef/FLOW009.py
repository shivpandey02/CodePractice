# cook your dish here
def total_expenses(items,price):
    total = items * price 
    discount = (total * 10)/100 
    if items > 1000:
        return '{:.6f}'.format(total-discount)
    return '{:.6f}'.format(total)
    
for i in range(int(input())):
    a,b = map(int,input().split())
    print(total_expenses(a,b))