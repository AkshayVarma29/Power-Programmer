# Given a list of sorted integers nums return the number of unique integers in the list.

nums = [2, 2, 2, 3, 4, 6, 6]

def solve(nums):
    uniq_set = set(nums)
    return len(uniq_set)

print(solve(nums))

# [Done] exited with code=0 in 0.11 seconds