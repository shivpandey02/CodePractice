# cook your dish here
def Possible_victory(r,o,c):
    if r > c:
        remian = r - c 
        remain_over = 20 - o 
        ball = remain_over * 6 
        run = ball*6 
        if run > remian:
            return 'YES'
        return 'NO'
    else:
        return 'YES'
    
    
r,o,c = map(int, input().split())        
print(Possible_victory(r,o,c))