# cook your dish here
def who_wins_the_bet(S_A, S_B, S_C):
  if S_C < S_A and S_C < S_B:
    return "Alice"
  elif S_B < S_A and S_B < S_C:
    return "Bob"
  elif S_A < S_B and S_A < S_C:
    return "Draw"
    
for i in range(int(input())):
    a,b,c = map(int,input().split())
    print(who_wins_the_bet(a,b,c))