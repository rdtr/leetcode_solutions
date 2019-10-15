# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        if root.left and not self.traverse(root.left, float('-inf'), root.val):
            return False
        if root.right and not self.traverse(root.right, root.val, float('inf')):
            return False
        return True

    def traverse(self, node, lower, upper):
        if node.val <= lower or node.val >= upper:
            return False
        if node.left and not self.traverse(node.left, lower, node.val):
            return False
        if node.right and not self.traverse(node.right, node.val, upper):
            return False
        return True
