# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return root

        cur = root
        stack = []

        while True:
            if cur.right:
                temp = cur.right
                stack.append(temp)
                cur.right = None
            if cur.left:
                cur.left, cur.right = cur.right, cur.left
                cur = cur.right
            else:
                if not stack:
                    return
                next = stack.pop()
                cur.right = next
                cur = cur.right
