# cook your dish here
def testing(friend_list, no_of_friend):
    left_friends = list(dict.fromkeys(friend_list))
    return len(left_friends)

for i in range(int(input())):
    k = int(input())
    friend = [int(i) for i in input().split()]
    print(testing(friend, k))
