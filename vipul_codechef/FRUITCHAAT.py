# cook your dish here
def chef_and_his_fruit_stand(x,y):
    apple = x//2
    if apple < y:
        print(apple)
    else:
        print(y)
        

for i in range(int(input())):
    a,b = map(int,input().split())
    chef_and_his_fruit_stand(a,b)