# cook your dish here
def tax_in_chefland(rupees):
    if rupees > 100:
        return rupees - 10
    return rupees
        
for i in range(int(input())):
    print(tax_in_chefland(int(input())))