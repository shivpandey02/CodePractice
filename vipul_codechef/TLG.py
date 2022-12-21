def find_winner(scores):
  # scores is a list of tuples containing the scores of each round
  # for each player in the format (player1_score, player2_score)
  player1_total = 0
  player2_total = 0
  max_lead = 0
  leader = None
  
  for score in scores:
    player1_total += score[0]
    player2_total += score[1]
    lead = player1_total - player2_total
    if abs(lead) > max_lead:
      max_lead = abs(lead)
      leader = 1 if lead > 0 else 2
  
  return leader,max_lead

# example usage
n = int(input())
scores = []
for i in range(n):
    a = tuple(int(item) for item in input().split()) 
    scores.append(a)
    
winner = find_winner(scores)
for i in winner:
    print(i,end = ' ')

    





        
        
            
    
        
