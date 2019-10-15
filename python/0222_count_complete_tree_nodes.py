# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0

        cur = root
        leftHeight = self.getHeight(cur.left)
        rightHeight = self.getHeight(cur.right)

        res = 0
        while True:
            if leftHeight == rightHeight:
                res += 2 ** leftHeight
                cur = cur.right
            else:
                res += 2 ** rightHeight
                cur = cur.left

            if not cur:
                break
            leftHeight = leftHeight - 1
            rightHeight = self.getHeight(cur.right)
        return res

    def getHeight(self, root):
        height = 0
        if not root:
            return height

        cur = root
        while cur:
            height += 1
            cur = cur.left
        return height
