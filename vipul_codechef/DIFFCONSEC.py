# cook your dish here
def different_consecutive_character(string):
    count = 0
    for i in range(len(string)-1):
        if string[i]==string[i+1]:
            count+=1 
    return count
    
for i in range(int(input())):
    k = int(input())
    print(different_consecutive_character(input()))
        
        