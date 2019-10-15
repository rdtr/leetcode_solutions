# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        res = []
        stack = []
        cur = root
        shouldGoRight = False

        while True:
            if not shouldGoRight and cur.left:
                stack.append(cur)
                cur = cur.left
                continue

            shouldGoRight = False
            res.append(cur.val)

            if cur.right:
                cur = cur.right
                continue
            if stack:
                shouldGoRight = True
                cur = stack.pop()
                continue
            break
        return res

