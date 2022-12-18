def mahasena(x,y):
    win = 0
    lose = 0
    for i in y:
        if i%2 == 0:
            win+=1 
        else:
            lose+=1
    if win>lose:
        print('READY FOR BATTLE')
    else:
        print('NOT READY')
        
    
n = int(input())
l = [int(i) for i in input().split()]
mahasena(n,l)