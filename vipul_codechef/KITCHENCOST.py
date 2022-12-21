# cook your dish here
def cost_of_groceries(number_of_item,minimum_fresh_value,l,cost):
    total_cost = 0
    for i in range(number_of_item):
        if l[i] >= minimum_fresh_value:
            total_cost += cost[i]
    return total_cost
            




for i in range(int(input())):
    number_of_item, minimum_fresh_value = map(int,input().split())
    l = [int(i) for i in input().split()]
    cost = [int(i) for i in input().split()]
    print(cost_of_groceries(number_of_item,minimum_fresh_value,l,cost))
    