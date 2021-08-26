# You are given a list of integers rooms and an integer target. 
# Return the first integer in rooms that's target or larger. If there is no solution, return -1.

rooms = [15, 10, 30, 50, 25]
target = 20

def solve(rooms, target):
    for value in rooms:
        if value>=target:
            return value
        else:
            pass
    return -1

print(solve(rooms, target))

# [Running] python -u "d:\Akshay\VSCode\power_programmer\first_fit_room.py"
# 30

# [Done] exited with code=0 in 0.117 seconds