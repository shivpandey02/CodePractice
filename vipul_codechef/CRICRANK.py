# cook your dish here
def cricket(player1,player2):
    player1_stat = 0
    player2_stat = 0
    for i in range(3):
        if player1[i] > player2[i]:
            player1_stat+=1 
        elif player2[i] > player1[i]:
                player2_stat+=1
                
    if player1_stat > player2_stat:
        return 'A'
    elif player2_stat > player1_stat:
        return 'B'

    
for i in range(int(input())):
    player1 = [int(i) for i in input().split()]
    player2 = [int(i) for i in input().split()]
    print(cricket(player1,player2))