# cook your dish here
def couples(g,b,length):
    #likeness = []
    #for i in range(length):
        #boy = max(b)
        #girl = min(g)
        #likeness.append((boy+girl))
        #b.remove(boy)
        #g.remove(girl)
    #return max(likeness)
    g.sort()
    b.sort(reverse = True)
    k = max([g[i]+b[i] for i in range(length)])
    return k
        
    
    
for i in range(int(input())):
    length = int(input())
    b = [int(i) for i in input().split()]
    g =[int(i) for i in input().split()]
    print(couples(g,b,length))
    
