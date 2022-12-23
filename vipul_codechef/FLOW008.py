# cook your dish here
def helping_chef(rating):
    if rating < 10:
        return 'Thanks for helping Chef!'
    else:
        return -1
        
for i in range(int(input())):
    print(helping_chef(int(input())))