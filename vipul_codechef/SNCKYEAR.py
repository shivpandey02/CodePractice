# cook your dish here
def snackdown(year):
    l = [2010, 2015, 2016, 2017, 2019]
    if year in l:
        return 'HOSTED'
    else:
        return 'NOT HOSTED'


for i in range(int(input())):
    print(snackdown(int(input())))