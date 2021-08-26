# Given a positive integer 'num', return sum of its digits. 
# Bonus - Can you do it without using strings?

from functools import reduce
num = 123
# def sum_of_digits(num):
#     num_list = list(str(num))
#     final = reduce(lambda a,b: int(a)+int(b), num_list)
#     return final

# [Done] exited with code=0 in 0.123 seconds

def sum_of_digits(num):
    sum_num = 0
    while (num!=0):
        sum_num += num % 10
        num = num // 10
    return sum_num

# [Done] exited with code=0 in 0.118 seconds

print(sum_of_digits(num))