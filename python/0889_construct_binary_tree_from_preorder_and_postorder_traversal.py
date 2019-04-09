# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if len(pre) == 0:
            return None

        p1, p2 = 1, 0
        root = TreeNode(pre[0])
        stack = [root]
        back = False
        while True:
            while stack and stack[-1].val == post[p2]:
                stack.pop()
                p2 += 1
                back = True

            if p1 == len(pre) and p2 == len(post):
                break

            newNode = TreeNode(pre[p1])
            if back:
                stack[-1].right = newNode
                stack.append(newNode)
            else:
                stack[-1].left = newNode
                stack.append(newNode)
            p1 += 1
            back = False
        return root
