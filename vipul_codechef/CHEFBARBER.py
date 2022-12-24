# cook your dish here
def salon(customer_number, time):
    return customer_number * time
    
for i in range(int(input())):
    a,b = map(int,input().split())
    print(salon(a,b))
