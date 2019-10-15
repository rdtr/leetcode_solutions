# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        prev = None
        cur = root
        stack = []
        leftVisited = False
        swapA = swapB = None

        while True:
            while cur and cur.left and not leftVisited:
                stack.append(cur)
                cur = cur.left
            leftVisited = False

            # visit
            if prev and prev.val > cur.val:
                if swapA is None:
                    swapA, swapB = prev, cur
                else:
                    swapB = cur
            prev = cur

            if cur.right:
                cur = cur.right
            elif stack:
                cur = stack.pop()
                leftVisited = True
            else:
                break

        swapA.val, swapB.val = swapB.val, swapA.val