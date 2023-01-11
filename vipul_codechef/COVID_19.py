# cook your dish here
def column(col):
    count = 0 
    for i in range(1,col+1,2):
        count+=1 
    return count
    
def row_(row):
    count = 0 
    for i in range(1,row+1,2):
        count+=1 
    return count
        
def main():
    for i in range(int(input())):
        row,col =map(int,input().split())
        x=column(col)
        y=row_(row)
        print(x*y)
        
main()
