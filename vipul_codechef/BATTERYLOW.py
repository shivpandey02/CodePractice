# cook your dish here
def battery(x):
    if x <= 15:
        print('Yes')
    else:
        print('No')
        
for i in range(int(input())):
    battery(int(input()))
        
