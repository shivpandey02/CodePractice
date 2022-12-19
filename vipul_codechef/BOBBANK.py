# cook your dish here
def bank(w,x,y,z):
    final_amount = w + (x*z) - (y*z)
    return final_amount
    
for i in range(int(input())):
    w,x,y,z = map(int,input().split())
    print(bank(w,x,y,z))