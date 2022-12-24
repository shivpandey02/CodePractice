# cook your dish here
def avoid_contact(x,y):
    if x == y:
        uninfected_people = x - y 
        return 2*y + uninfected_people -1
         
    else:
        uninfected_people = x - y 
        bad_required = 2*y + uninfected_people 
        return bad_required 
        
for i in range(int(input())):
    a,b = map(int,input().split())
    print(avoid_contact(a,b))
        
        