# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return False

        q = deque([root])
        isBottom = False
        while q:
            qlen = len(q)
            noChild = False
            for i in range(qlen):
                node = q.popleft()
                if node.left:
                    if isBottom or noChild:
                        return False
                    q.append(node.left)
                else:
                    noChild = True

                if node.right:
                    if isBottom or noChild:
                        return False
                    q.append(node.right)
                else:
                    noChild = True

            if noChild:
                isBottom = True
        return True