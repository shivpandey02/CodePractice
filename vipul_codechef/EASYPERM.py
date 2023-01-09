# cook your dish here
def easy_permutation(number):
    arr = list(range(1,number+1))
    return arr[::-1]
    
for i in range(int(input())):
    k = easy_permutation(int(input()))
    print(*k)

