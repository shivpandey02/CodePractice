# cook your dish here
def olympics_ranking(country1):
    medal_of_country1 = sum((country1)[0:len(country1)//2])
    medal_of_country2 = sum((country1)[len(country1)//2:])
    if medal_of_country1 > medal_of_country2:
        return 1 
    else:
        return 2 
        
        
for i in range(int(input())):
    a = list(int(i) for i in input().split())
    print(olympics_ranking(a))