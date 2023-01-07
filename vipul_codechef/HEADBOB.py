# cook your dish here
def gesture(string):
    if 'I' in string:
        return 'INDIAN'
    if 'Y' in string:
        return 'NOT INDIAN'
    else:
        return 'NOT SURE'
    
for i in range(int(input())):
    k = int(input())
    string = input()
    print(gesture(string))
    