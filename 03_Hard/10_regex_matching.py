# Implement regular expression matching with the following special characters:
#     . (period) which matches any single character
#     * (asterisk) which matches zero or more of the preceding element
# That is, implement a function that takes in a valid regular expression pattern and a string s and returns whether or not the string matches the regular expression.
# Note: The input pattern is guaranteed not to have consecutive asterisks.

pattern = "ra."
s = "ray" # True

# pattern = "a"
# s = "aa" # False

# pattern = "a*"
# s = "aa" # True

# pattern = ".*"
# s = "abc" # True

import re
def solve(pattern, s):
    if pattern.startswith ('*'):
        return False
    final = re.findall(pattern,s)
    if s in final and len(final)!=0:
        return True
    return False

print(solve(pattern,s))

# [Done] exited with code=0 in 0.124 seconds