# cook your dish here
def high_accuracy(m):
    correct = m//3
    if m%3 == 0:
        return 0
    else:
        incorrect_answer =  (correct*3) + 3 - m
        return incorrect_answer
    
    
for i in range(int(input())):
    print(high_accuracy(int(input())))