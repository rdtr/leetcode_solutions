from collections import deque


class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if root is None:
            return []

        res = []
        q = deque([root])
        while q:
            qlen = len(q)
            tmp = []
            for i in range(qlen):
                node = q.popleft()
                tmp.append(node.val)

                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            res.append(tmp)
        return res