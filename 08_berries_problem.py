# There are 2 types of Berries. Pineapple and Banana berries. 
# Given that each Banana berry gives you exactly K calaries and each Pineapple berry gives 1 calorie.
# Determine the number of ways in which you can eat the berries to gain exactly N calories.

# Sample input N = 1 and K = 5 =======> you can eat only 1 pineapple berry.
# Sample input N = 5 and K = 3 =======> you can eat 5 calories in 4 ways. 
# Sample input N = 4 and K = 2 ======> you can eat 4 calories in 5 ways.

N = 4
K = 2
cal = [1,K]
result = []

def determine_count(comb,result,target):
    if sum(comb) == target:
        result.append(list(comb))
    elif sum(comb) > target:
        return

    for i in cal:
        comb.append(i)
        determine_count(comb,result,target)
        comb.pop(-1)

    
determine_count([],result,N)
print('Total Possible Ways are ' + str(len(result)) + '\n')
print(result)

# Total Possible Ways are 5

# [[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2]]

# [Done] exited with code=0 in 0.112 seconds