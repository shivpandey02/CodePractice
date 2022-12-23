# cook your dish here
def farmers_league(N):
    return 3 * (N//2)
    
for i in range(int(input())):
    print(farmers_league(int(input())))