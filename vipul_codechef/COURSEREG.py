# cook your dish here
def course_registration(n,x,y):
    if x - y >= n:
        return 'Yes'
    else:
        return 'No'


for i in range(int(input())):
    n,x,y = map(int, input().split())
    print(course_registration(n,x,y))