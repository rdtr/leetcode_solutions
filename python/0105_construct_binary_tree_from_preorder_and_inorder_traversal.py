# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        num = len(preorder)
        if num == 0:
            return None

        inpos = {}
        for i, val in enumerate(inorder):
            inpos[val] = i

        root = TreeNode(preorder[0])
        stack = []
        cur = root

        for i in range(1, num):
            if inpos[cur.val] > inpos[preorder[i]]:
                stack.append(cur)
                cur.left = TreeNode(preorder[i])
                cur = cur.left
            else:
                while stack and inpos[stack[-1].val] < inpos[preorder[i]]:
                    cur = stack.pop()
                cur.right = TreeNode(preorder[i])
                cur = cur.right
        return root