# cook your dish here
def gross_salary(salary):
    if salary < 1500:
        hra = salary * 0.10
        da = salary * 0.90
        return salary + hra + da
    else:
        hra = 500
        da = salary * 0.98
        return salary + hra + da
        
for i in range(int(input())):
    print(gross_salary(int(input())))