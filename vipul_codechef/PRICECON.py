# cook your dish he
def price_control(l1, l2):
    price_cap = l1[-1]
    sum_before_price_cap = sum(l2)
    sum_after_price_cap = 0
    for price in l2:
        if price > price_cap:
            sum_after_price_cap += price_cap
        else:
            sum_after_price_cap += price
    if sum_after_price_cap < sum_before_price_cap:
        return sum_before_price_cap - sum_after_price_cap
    else:
        return 0 
        
for i in range(int(input())):
    l1 = [int(i) for i in input().split()]
    l2 = [int(i) for i in input().split()]
    print(price_control(l1,l2))
            
