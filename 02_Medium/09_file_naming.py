# You are given an array of desired filenames in the order of their creation.
# Since two files cannot have equal names, the one which comes later will have an addition
# to its name in a form of (k) where k is smallest positive integer such that obtained name is not used yet.
# Return the array of names that will be given to the files. 

# Example - names = ['doc','doc','image','doc(1)','doc']
# fileNaming(names) = ['doc','doc(1)','image','doc(1)(1)','doc(2)']

names = ['doc','doc','image','doc(1)','doc']
result = []

def fileNaming(names):
    version = {x:0 for x in names}
    for name in names:
        if version[name] == 0 and name not in result:
            result.append(name)
        else:
            version[name] += 1
            result.append(name + '(' + str(version[name]) + ')')
    return result

print(fileNaming(names))

# ['doc', 'doc(1)', 'image', 'doc(1)(1)', 'doc(2)']

# [Done] exited with code=0 in 0.109 seconds