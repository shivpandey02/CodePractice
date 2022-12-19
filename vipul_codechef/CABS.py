# cook your dish here
def cabeservice(mrp1,mrp2):
    if mrp2>mrp1:
        return 'FIRST'
    elif mrp1>mrp2:
        return 'SECOND'
    else:
        return 'ANY'
        
number = int(input())
for i in range(number):
    i = [int(i) for i in input().split()]
    print(cabeservice(i[0],i[1]))
