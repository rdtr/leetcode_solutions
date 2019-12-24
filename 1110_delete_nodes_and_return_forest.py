# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return []

        res = []
        deleteSet = set(to_delete)

        if root.val in deleteSet:
            self.helper(res, root.left, None, deleteSet, True)
            self.helper(res, root.right, None, deleteSet, False)
        else:
            res.append(root)
            self.helper(res, root.left, root, deleteSet, True)
            self.helper(res, root.right, root, deleteSet, False)

        return res

    def helper(self, res, cur, parent, deleteSet, isLeft):
        if not cur:
            return

        if cur.val in deleteSet:
            if parent:
                if isLeft:
                    parent.left = None
                else:
                    parent.right = None
            self.helper(res, cur.left, None,  deleteSet, True)
            self.helper(res, cur.right, None, deleteSet, False)
        else:
            if not parent:
                res.append(cur)
            self.helper(res, cur.left, cur, deleteSet, True)
            self.helper(res, cur.right, cur, deleteSet, False)
