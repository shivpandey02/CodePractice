# cook your dish here
def chef_on_land(x,y,xi,yi,d):
    if x//xi>=d and y//yi>=d:
        return 'Yes'
    
    return 'No'
    
for i in range(int(input())):
    x,y,xi,yi,d = map(int, input().split())
    print(chef_on_land(x,y,xi,yi,d))