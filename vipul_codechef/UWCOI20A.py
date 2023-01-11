# cook your dish here
def peak_finding(number):
    maximum = max(number)
    return maximum 
    
for i in range(int(input())):
    k = int(input())
    l = []
    for i in range(k):
        l.append(int(input()))
    print(peak_finding(l))
        
        
