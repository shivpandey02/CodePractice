# cook your dish here
def credit_score(x):
    if x>=750:
        return 'YES'
    else:
        return 'NO'
        
n = int(input())
print(credit_score(n))