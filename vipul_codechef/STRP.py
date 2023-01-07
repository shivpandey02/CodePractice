def string_protocol(string,n):
    count = 0 
    i = 0
    if len(string) == 0:
        return 0
    if len(string) == 1:
        return 1
    while True:
        if string[i]==string[i+1]:
            count+=1
            string = string[i+2:]
        else:
            string = string[i+1:]
            count+=1
        if len(string)==0:
            count+=0
            return count
        if len(string)==1:
            count+=1
            return count
    
for i in range(int(input())):
    k = int(input())
    string = input()
    print(string_protocol(string,k))
    

        