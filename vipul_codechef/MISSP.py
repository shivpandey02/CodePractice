def find_missing_doll(dolls):
    # Use a set to store the dolls we have seen
    seen = set()
    # Iterate through the dolls
    for doll in dolls:
        # If we have seen the doll before, remove it from the set
        if doll in seen:
            seen.remove(doll)
        # Otherwise, add it to the set
        else:
            seen.add(doll)
    # The remaining doll in the set is the missing one
    return seen.pop()

# Read the number of test cases
t = int(input())

# Iterate through the test cases
for _ in range(t):
    # Read the number of dolls
    n = int(input())
    # Read the doll types
    dolls = [input().strip() for _ in range(n)]
    # Find the missing doll and print it
    print(find_missing_doll(dolls))
