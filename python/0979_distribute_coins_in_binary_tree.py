# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        res = [0]
        self.helper(root, res)
        return res[0]

    def helper(self, node, res):
        if not node:
            return 0

        lmove = self.helper(node.left, res)
        rmove = self.helper(node.right, res)

        res[0] += abs(lmove) + abs(rmove)
        return node.val + lmove + rmove - 1