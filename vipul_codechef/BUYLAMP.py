# cook your dish here
def Buy(n,k,x,y):
    blue_lamp = n - k
    cost_of_red_lamp = k*x 
    if x > y:
        total_cost = blue_lamp * y + cost_of_red_lamp 
        return total_cost 
    return n*x

for i in range(int(input())):
    a,b,c,d = map(int,input().split())
    print(Buy(a,b,c,d))