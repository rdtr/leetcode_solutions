class Solution:
    def splitBST(self, root, V):
        """
        :type root: TreeNode
        :type V: int
        :rtype: List[TreeNode]
        """

        if root is None:
            return [None, None]

        cur = root
        if cur.val > V:
            splitted = self.splitBST(cur.left, V)
            cur.left = splitted[1]
            return [splitted[0], cur]
        else:
            splitted = self.splitBST(cur.right, V)
            cur.right = splitted[0]
            return [cur, splitted[1]]