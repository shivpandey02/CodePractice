# cook your dish here
def dna(string,k):
    st = ''
    for i in range(0,k,2):
        if string[i:i+2] == '00':
            st+='A'
        elif string[i:i+2] == '01':
            st+='T'
        elif string[i:i+2] == '10':
            st+='C'
        elif string[i:i+2] == '11':
            st+='G'
    return st

for i in range(int(input())):
    k = int(input())
    string = input()
    print(dna(string,k))