# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        return self.traverse(root.left, root.right)

    def traverse(self, left, right):
        if not left and not right:
            return True
        elif (not left and right) or (left and not right) or (left.val != right.val):
            return False

        return self.traverse(left.left, right.right) and self.traverse(left.right, right.left)