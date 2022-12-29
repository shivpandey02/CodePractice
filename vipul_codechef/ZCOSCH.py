# cook your dish here
def schlorship(marks):
    if 1<=marks<=50:
        return 100 
    elif 51<=marks<=100:
        return 50 
    else:
        return 0 
        
print(schlorship(int(input())))