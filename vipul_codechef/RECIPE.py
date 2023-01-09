import math
def cutting_recipes(ratios):
    k = ratios.pop(0)
    common_factor = math.gcd(*ratios)
    return [x//common_factor for x in ratios]
    
t = int(input())
for _ in range(t):
    ratios = list(map(int, input().split()))
    output = cutting_recipes(ratios)
    print(*output)

    
