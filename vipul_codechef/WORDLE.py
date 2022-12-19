# cook your dish here
def wordle(m,n):
    length = len(m)
    string = ''
    for i in range(0,length):
        if m[i] == n[i]:
            string +='G'
        else:
            string +='B'
    return string
            
n = int(input())
for i in range(n):
    m = input()
    n = input()
    print(wordle(m,n))
            