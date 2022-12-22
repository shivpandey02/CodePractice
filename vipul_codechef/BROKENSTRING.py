# cook your dish here

def broken_string(string):
    order = len(string)//2
    s1 = string[:order]
    s2 = string[order:]
    for i in range(0,order):
        if string[i] != string[i+order]:
            return 'NO'
    return 'YES'
    
for i in range(int(input())):
    k = int(input())
    l = input()
    print(broken_string(l))