# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 and t2:
            t1.val += t2.val
            if t1.left and t2.left:
                self.helper(t1.left, t2.left)
            elif t2.left:
                t1.left = TreeNode(0)
                self.helper(t1.left, t2.left)

            if t1.right and t2.right:
                self.helper(t1.right, t2.right)
            elif t2.right:
                t1.right = TreeNode(0)
                self.helper(t1.right, t2.right)
            return t1
        elif t1:
            return t1
        else:
            return t2

    def helper(self, n1, n2):
        n1.val += n2.val

        if n1.left and n2.left:
            self.helper(n1.left, n2.left)
        elif n2.left:
            n1.left = TreeNode(0)
            self.helper(n1.left, n2.left)

        if n1.right and n2.right:
            self.helper(n1.right, n2.right)
        elif n2.right:
            n1.right = TreeNode(0)
            self.helper(n1.right, n2.right)
