# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        plen = len(preorder)
        if plen == 0:
            return None

        root = TreeNode(preorder[0])
        cur = root
        stack = [root]

        for i in range(1, plen):
            if preorder[i] < cur.val:
                stack.append(cur)
                cur.left = TreeNode(preorder[i])
                cur = cur.left
            elif not stack:
                cur.right = TreeNode(preorder[i])
                cur = cur.right
            else:
                while stack and stack[-1].val < preorder[i]:
                    cur = stack.pop()
                cur.right = TreeNode(preorder[i])
                cur = cur.right
        return root