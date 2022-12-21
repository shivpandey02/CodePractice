# cook your dish here
def count_problem(contest_codes):
    # Initialize counters for each contest
    start38_count = 0
    ltime108_count = 0

    # Iterate through the contest codes and count the problems for each contest
    for i in contest_codes:
        if i == 'START38':
            start38_count+=1
        else:
            ltime108_count+=1 
    # Return the count of problems for each contest
    return (start38_count,ltime108_count)

for i in range(int(input())):
    a = int(input())
    lst = [i for i in input().split()]
    answer = count_problem(lst)
    print(*answer)