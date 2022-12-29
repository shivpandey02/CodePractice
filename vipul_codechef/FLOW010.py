# cook your dish here
def id_and_ship(string):
    if string == 'b':
        return 'BattleShip'
    elif string =='c':
        return 'Cruiser'
    elif string == 'd':
        return 'Destroyer'
    elif string == 'f':
        return 'Frigate'
        
for i in range(int(input())):
    print(id_and_ship(input().lower()))
