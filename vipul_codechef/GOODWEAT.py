# cook your dish here
def good_weather(weather):
    good_days = weather.count(1)
    bad_days = weather.count(0)
    if good_days > bad_days:
        print('Yes')
    else:
        print('NO')
    
for i in range(int(input())):
    weather = [int(i) for i in input().split()]
    good_weather(weather)