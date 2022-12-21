# cook your dish here
def is_eligible_for_exam(minimum_age_limit, maximum_age_limit, chef_age):
    if minimum_age_limit <= chef_age < maximum_age_limit:
        return 'yes'
    else:
        return 'no'
        
for i in range(int(input())):
    a,b,c = map(int, input().split())
    print(is_eligible_for_exam(a,b,c))