def matches_needed(A, B):
    sum_of_a_b = A + B
    sum_str = str(sum_of_a_b)
    matches_needed = 0
    for digit in sum_str:
        if digit == "1":
            matches_needed += 2
        elif digit == "2":
            matches_needed += 5
        elif digit == "3":
            matches_needed += 5
        elif digit == "4":
            matches_needed += 4
        elif digit == "5":
            matches_needed += 5
        elif digit == "6":
            matches_needed += 6
        elif digit == "7":
            matches_needed += 3
        elif digit == "8":
            matches_needed += 7
        elif digit == "9":
            matches_needed += 6
        else:
            # Assume the digit is 0
            matches_needed += 6
    return matches_needed

for i in range(int(input())):
    x,y = map(int,input().split())
    print(matches_needed(x,y))
        
    
                                                                       