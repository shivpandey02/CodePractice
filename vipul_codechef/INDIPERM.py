# cook your h here
def permutation(number):
    num = list(range(1,number+1))
    if number==2:
        return ([2,1])
    else:
        for i in range(1, number - 1):
            num[i], num[i + 1] = num[i + 1], num[i]
        return num
    
for i in range(int(input())):
    output = permutation(int(input()))
    print(*output)