# cook your dish here
def tour_of_king(n,m):
    return (n*5) + (m*7)
    
for i in range(int(input())):
    n,m = input().split()
    print(tour_of_king(int(n),int(m)))