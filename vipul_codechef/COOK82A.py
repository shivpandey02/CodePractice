# cook your dish here
def la_liga(d):
    if d['RealMadrid']<d['Malaga'] and d['Barcelona']>d['Eibar']:
        return "Barcelona"
    else:
        return 'RealMadrid'
    
    

d = {}
for i in range(int(input())):
    for i in range(4):
        key,value = map(str,input().split())
        d[key] = int(value)
    print(la_liga(d))
    
    
    