# cook your dish here
def candy(a,b):
    candy_to_each_friend = a/b 
    if candy_to_each_friend%2 == 0:
        return 'Yes'
    else:
        return 'No'
        
for i in range(int(input())):
    a = [int(i) for i in input().split()]
    print(candy(a[0],a[1]))