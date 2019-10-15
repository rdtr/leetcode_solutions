# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        leftHeight, leftOK = self.getHeight(root.left)
        rightHeight, rightOK = self.getHeight(root.right)
        if not (leftOK and rightOK):
            return False
        return abs(leftHeight - rightHeight) <= 1

    def getHeight(self, node):
        if node is None:
            return 0, True

        leftHeight, leftOK = self.getHeight(node.left)
        rightHeight, rightOK = self.getHeight(node.right)
        if not (leftOK and rightOK):
            return 0, False
        elif abs(leftHeight - rightHeight) > 1:
            return 0, False
        return max(leftHeight, rightHeight) + 1, True
