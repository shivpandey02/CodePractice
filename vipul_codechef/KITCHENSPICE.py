# cook your dish here
def spice_level(level):
    if level < 4:
        return 'MILD'
    elif 4 <= level < 7:
        return 'MEDIUM'
    elif level >=7:
        return 'HOT'
        
for i in range(int(input())):
    print(spice_level(int(input())))