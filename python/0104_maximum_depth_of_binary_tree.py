# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res = [1]
        if root.left:
            self.helper(root.left, 2, res)
        if root.right:
            self.helper(root.right, 2, res)
        return res[0]

    def helper(self, cur, curDepth, res):
        if cur.left:
            self.helper(cur.left, curDepth + 1, res)
        if cur.right:
            self.helper(cur.right, curDepth + 1, res)

        if cur.left is None and cur.right is None:
            res[0] = max(res[0], curDepth)
