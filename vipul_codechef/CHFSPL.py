# cook your dish here
def spell(l):
    l.sort() 
    return l[-1] + l[-2]
    
for i in range(int(input())):
    l = [int(i) for i in input().split()]
    print(spell(l))
    