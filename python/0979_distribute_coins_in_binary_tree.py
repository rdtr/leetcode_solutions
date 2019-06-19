class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        res = [0]
        l = r = 0
        if root.left:
            l = helper(root.left, res)
        if root.right:
            r = helper(root.right, res)
        return res[0] + abs(l) + abs(r)


def helper(root, res):
    if not root.left and not root.right:
        return root.val - 1

    l = r = 0
    if root.left:
        l = helper(root.left, res)
    if root.right:
        r = helper(root.right, res)
    res[0] = res[0] + abs(l) + abs(r)
    return root.val + l + r - 1