# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        ppath, qpath = [], []
        self.find(root, p, ppath)
        self.find(root, q, qpath)

        i = 0
        while i < len(ppath) and i < len(qpath):
            if ppath[i] == qpath[i]:
                i += 1
                continue
            break
        return ppath[i - 1]

    def find(self, parent, target, path):
        path.append(parent)
        if parent.val == target.val or (parent.left and self.find(parent.left, target, path)) or (
                parent.right and self.find(parent.right, target, path)):
            return True
        path.pop()
        return False
