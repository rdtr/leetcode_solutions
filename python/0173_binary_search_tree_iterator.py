# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root):
        """
        :type root: TreeNode
        """

        self.stack = []
        cur = root
        while cur:
            self.stack.append(cur)
            cur = cur.left

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """

        res = self.stack.pop()
        cur = res
        if cur.right:
            cur = cur.right
            while cur:
                self.stack.append(cur)
                cur = cur.left
        return res.val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """

        return len(self.stack) > 0