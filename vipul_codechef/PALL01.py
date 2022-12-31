# cook your dish here
def game(number):
    string = str(number)
    reverse = string[::-1]
    if number == int(reverse):
        return 'wins'
    return 'loses'

for i in range(int(input())):
    print(game(int(input())))