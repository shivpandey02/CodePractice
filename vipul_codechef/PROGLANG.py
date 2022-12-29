# cook your dish here
def languages(a,b,c,d,e,f):
    using_language = [a,b]
    switch1 = [c,d]
    switch2 = [e,f] 
    using_language.sort()
    switch1.sort() 
    switch2.sort()
    if using_language == switch1:
        return 1
    elif using_language == switch2:
        return 2
    return 0
    
for i in range(int(input())):
    a,b,c,d,e,f = map(int,input().split())
    print(languages(a,b,c,d,e,f))