class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        if not root:
            return

        l = r = False
        if root.left:
            l = self.helper(root.left, root.val, limit)
            if not l:
                root.left = None
        if root.right:
            r = self.helper(root.right, root.val, limit)
            if not r:
                root.right = None

        if not l and not r:
            return None
        return root

    def helper(self, root, curSum, limit):
        newSum = curSum + root.val
        if not root.left and not root.right:
            return newSum >= limit

        l = r = False
        if root.left:
            l = self.helper(root.left, newSum, limit)
            if not l:
                root.left = None
        if root.right:
            r = self.helper(root.right, newSum, limit)
            if not r:
                root.right = None

        return l or r