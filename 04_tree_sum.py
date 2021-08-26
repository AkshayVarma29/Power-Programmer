# Given a binary tree root, return the sum of all values in the tree.

# Tree Representation
root = [1, [2, None, ], [3, [5, None, None], None]]

def solve(root):
    if root == None:
        return 0
    return root.val + solve(root.left) + solve(root.right)

print(solve(root))
