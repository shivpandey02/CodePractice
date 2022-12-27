# cook your dish here
'''def construct_n(number):
    seven = number%7
    two = seven%2 
    if two==0:
        return 'YES'
    return 'NO'
    
for i in range(int(input())):
    print(construct_n(int(input())))'''
    
for _ in range(int(input())):
    h=int(input())
    k=h%7
    if(h<7 and h%2!=0):
        print("no")
    else:
        print("yES")
    
    
    
