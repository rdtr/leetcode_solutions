# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        sumMap = defaultdict(lambda: 0)
        if not root:
            return 0

        res = [0] if root.val != sum else [1]  # just use array to pass as reference
        sumMap[root.val] = 1
        if root.left:
            self.helper(root.left, sumMap, sum, root.val, res)
        if root.right:
            self.helper(root.right, sumMap, sum, root.val, res)
        return res[0]

    def helper(self, cur, sumMap, sum, sumSoFar, res):
        sumSoFar += cur.val
        if sumSoFar == sum:
            res[0] += 1
        res[0] += sumMap[sumSoFar - sum]

        sumMap[sumSoFar] += 1
        if cur.left:
            self.helper(cur.left, sumMap, sum, sumSoFar, res)
        if cur.right:
            self.helper(cur.right, sumMap, sum, sumSoFar, res)
        sumMap[sumSoFar] -= 1