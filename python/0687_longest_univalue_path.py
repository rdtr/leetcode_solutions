# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root:
            return 0

        res = [0]
        leftpath = rightpath = 0
        if root.left:
            if root.val == root.left.val:
                leftpath = 1 + self.helper(root.left, root.val, 1, res)
            else:
                self.helper(root.left, root.val, 0, res)
        if root.right:
            if root.val == root.right.val:
                rightpath = 1 + self.helper(root.right, root.val, 1, res)
            else:
                self.helper(root.right, root.val, 0, res)
        return max(res[0], leftpath + rightpath)

    def helper(self, node, parentVal, cur, res):
        leftpath = rightpath = 0
        if node.left:
            if node.val == node.left.val:
                leftpath = 1 + self.helper(node.left, node.val, cur + 1, res)
            else:
                res[0] = max(res[0], cur)
                self.helper(node.left, node.val, 0, res)
        if node.right:
            if node.val == node.right.val:
                rightpath = 1 + self.helper(node.right, node.val, cur + 1, res)
            else:
                res[0] = max(res[0], cur)
                self.helper(node.right, node.val, 0, res)
        res[0] = max(res[0], leftpath + rightpath)
        return max(leftpath, rightpath)




