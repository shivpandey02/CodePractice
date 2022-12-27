# cook your dish here
class ImportantPages:
    def __init__(self,l):
        self.a = l[0]
        self.b = l[1] 
        self.codechef_mail()
        
    def codechef_mail(self):
        if self.a == 0:
            print("https://www.codechef.com/practice")
        elif self.b == 0:
            print('https://www.codechef.com/contests')
        else:
            print("https://discuss.codechef.com")
            
l = [int(i) for i in input().split()]
t = ImportantPages(l)