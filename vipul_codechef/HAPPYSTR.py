# cook your dish here
def happy_string(string):
    v = 'aeiou'
    count = 0 
    maximum = 0
    length = len(string)
    for i in range(length-1):
        if string[i] and string[i+1] in v:
            count+=1
            if maximum < count:
                maximum = count
        else:
            count = 0 
    if maximum > 2:
        return 'Happy'
    return 'Sad'
    
for i in range(int(input())):
    print(happy_string(input()))
        