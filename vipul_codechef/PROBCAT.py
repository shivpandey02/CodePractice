# cook your dish here
def problem_category(x):
    if 1 <= x < 100 :
        return 'Easy'
    elif x < 200:
        return 'Medium'
    elif 200 <= x <= 300:
        return 'Hard'
        
for i in range(int(input())):
    print(problem_category(int(input())))