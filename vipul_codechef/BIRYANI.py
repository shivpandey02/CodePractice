# cook your dish here
def total_cost_of_classes(weeks, cost_per_week):
    return weeks * cost_per_week
    
for i in range(int(input())):
    week,cost_per_week = map(int, input().split())
    print(total_cost_of_classes(week,cost_per_week))