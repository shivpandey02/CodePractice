# cook your dish here
class ComplementaryStrand:
    def __init__(self,string,length):
        self.string = string 
        self.length = length 
        self.Complementary()
        
    def Complementary(self):
        st = ''
        for i in range(self.length):
            if self.string[i] == 'A':
                st+='T'
            elif self.string[i] == 'T':
                st+='A'
            elif self.string[i] == 'C':
                st+='G'
            elif self.string[i] =='G':
                st+='C'
        print(st)
                
        
for i in range(int(input())):
    l = int(input())
    string = input()
    t = ComplementaryStrand(string,l)