# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0

        leftVal, rightVal, res = 1, 1, [0]
        if root.left:
            leftVal = self.doLongestConsecutive(root.left, res)
            if root.val == root.left.val - 1:
                leftVal += 1
        if root.right:
            rightVal = self.doLongestConsecutive(root.right, res)
            if root.val == root.right.val - 1:
                rightVal += 1
        return max(res[0], leftVal, rightVal)

    def doLongestConsecutive(self, node, res):
        leftVal, rightVal = 1, 1
        if node.left:
            leftVal = self.doLongestConsecutive(node.left, res)
            if node.val == node.left.val - 1:
                leftVal += 1
                res[0] = max(res[0], leftVal)
            else:
                leftVal = 1
        if node.right:
            rightVal = self.doLongestConsecutive(node.right, res)
            if node.val == node.right.val - 1:
                rightVal += 1
                res[0] = max(res[0], rightVal)
            else:
                rightVal = 1
        return max(leftVal, rightVal)
