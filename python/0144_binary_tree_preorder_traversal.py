class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        cur = root
        s = []
        res = []
        while True:
            res.append(cur.val)

            if cur.left:
                if cur.right:
                    s.append(cur.right)
                cur = cur.left
            elif cur.right:
                cur = cur.right
            elif s:
                cur = s.pop()
            else:
                break
        return res
