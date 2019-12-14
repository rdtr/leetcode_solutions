# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        res = 0
        cur = root
        while cur:
            leftHeight = self.checkHeight(cur.left)
            rightHeight = self.checkHeight(cur.right)
            if leftHeight == rightHeight:
                res += self.count(leftHeight) + 1
                cur = cur.right
            else:
                res += self.count(rightHeight) + 1
                cur = cur.left
        return res
        
    def checkHeight(self, root):
        res = 0
        cur = root
        while cur:
            res += 1
            cur = cur.left
        return res
        
    def count(self, height):
        if height == 0:
            return 0
        return (2 ** height) - 1
