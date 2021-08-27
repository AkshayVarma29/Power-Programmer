# Given a list of integers nums, return a new list such that each element at index i of the new list is the 
# product of all the numbers in the original list except the one at i. 
# Do this without using division.

nums = [1, 2, 3, 4, 5]

def solve(nums):
    new_list = []
    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if i!=j:
                product = product*nums[j]
            else:
                pass
        new_list.append(product)
    return new_list

print(solve(nums))

