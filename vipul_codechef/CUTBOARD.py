# cook your dish here
def cut_the_board(n,m):
    return (n-1)*(m-1)
    
for i in range(int(input())):
    x,y = map(int,input().split())
    print(cut_the_board(x,y))
