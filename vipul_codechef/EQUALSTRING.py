# cook your dish here
def equal_string(string1,string2,length):
    new_string= ''
    for i in range(length):
        if string1[i]!=string2[i]:
            if string2[i] not in new_string:
                new_string+=string2[i]
    return len(new_string)

for i in range(int(input())):
    length = int(input())
    string1 = input()
    string2 = input()
    print(equal_string(string1,string2,length))
