# cook your dish here
def number_of_unattempted(unattempted,attempted):
    return unattempted - attempted
    
a,b = map(int, input().split())
print(number_of_unattempted(a,b))