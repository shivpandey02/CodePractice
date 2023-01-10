# cook your dish here
def stock(s,a,b,c):
    drop_up_share_price = (s*c)/100 
    final_price = s + drop_up_share_price
    if a<=final_price<=b:
        return 'yes'
    return 'no'
    
for i in range(int(input())):
    s,a,b,c = map(int,input().split())
    print(stock(s,a,b,c))

