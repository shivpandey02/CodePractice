# cook your dish here
def highest_divide(intger):
    t = 9 
    while True:
        if intger%t == 0:
            return t
            break  
        t-=1
        
print(highest_divide(int(input())))