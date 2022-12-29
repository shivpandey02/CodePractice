# cook your dish here
def equal(m):
    if m == 3:
        return '010'
    else:
        string = '1'
        for i in range(m-2):
            string+='0'
        string+='1' 
    return string 
    
for i in range(int(input())):
    print(equal(int(input())))