# cook your dish here
def indivisible(a,b,c):
    number = 1 
    while True:
        if a%number!=0 and b%number!=0 and c%number!=0:
            break
        number+=1
        
        
        
    return number 
    
for i in range(int(input())):
    a,b,c = input().split()
    print(indivisible(int(a),int(b),int(c)))
    
    
        
        
    