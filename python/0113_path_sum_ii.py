# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        
        if not root:
            return []

        res = []
        self.doPathSum(root, sum, 0, [], res)
        return res
        
    def doPathSum(self, node, sum, curSum, cur, res):
        if node.left is None and node.right is None:
            if curSum + node.val == sum:
                cur.append(node.val)
                res.append(cur.copy())
                cur.pop()
            return
        
        cur.append(node.val)
        if node.left is not None:
            self.doPathSum(node.left, sum, curSum + node.val, cur, res)
        if node.right is not None:
            self.doPathSum(node.right, sum, curSum + node.val, cur, res)
        cur.pop()
