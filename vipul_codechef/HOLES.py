# cook your dish here
def holes_in_index(string):
    hole = ["A", "D", "O", "P", "R",'Q']
    count = 0
    for i in string:
        if i in hole:
            count+=1 
        if i == 'B':
            count+=2 
    return count 
    
for i in range(int(input())):
    print(holes_in_index(input()))
