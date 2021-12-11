# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None or root.left is None:
            return root
        container = []
        self.helper(root, root.left, root.right, container)
        root.left = None
        root.right = None

        return container[0]

    def helper(self, parent, cur, right, container):
        if cur.left:
            self.helper(cur, cur.left, cur.right, container)
        else:
            container.append(cur)

        cur.left = right
        cur.right = parent



