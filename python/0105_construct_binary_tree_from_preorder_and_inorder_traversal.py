# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) <= 0:
            return None

        inmap = {n: i for i, n in enumerate(inorder)}
        root = TreeNode(preorder[0])

        stack = [root]
        i = 1
        while i < len(preorder):
            node = TreeNode(preorder[i])
            if inmap[stack[-1].val] > inmap[node.val]:
                stack[-1].left = node
                stack.append(node)
            else:
                while stack and inmap[stack[-1].val] < inmap[node.val]:
                    prev = stack.pop()
                prev.right = node
                stack.append(node)
            i += 1
        return root