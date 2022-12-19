# cook your dish here
def number_of_mangoes(x,y,z):
    mangoes = z - y  
    return mangoes//x
    
for i in range(int(input())):
    x,y,z = map(int,input().split())
    print(number_of_mangoes(x,y,z))