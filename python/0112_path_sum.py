# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        
        if root is None:
            return False
        
        if root.val == sum and root.left is None and root.right is None:
            return True
        left = self.doHasPathSum(root.left, root.val, sum) if root.left is not None else False
        right = self.doHasPathSum(root.right, root.val, sum) if root.right is not None else False
        return left or right
        
    def doHasPathSum(self, node, cur, target):
        sum = cur + node.val
        if sum == target and node.left is None and node.right is None:
            return True
        
        left = self.doHasPathSum(node.left, sum, target) if node.left is not None else False
        right = self.doHasPathSum(node.right, sum, target) if node.right is not None else False
        return left or right