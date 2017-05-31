class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return result

        numsSoFar = []
        sumSoFar = 0
        self.doPathSum(root, sum, numsSoFar, sumSoFar, result)
        return result

    def doPathSum(self, parent, target, numsSoFar, sumSofar, result):
        if not parent:
            return
        if sumSofar + parent.val == target:
            if not parent.left and not parent.right:
                numsSoFar.append(parent.val)
                result.append(numsSoFar)
                return

        sumSofar += parent.val
        numsSoFar.append(parent.val)
        self.doPathSum(parent.left, target, numsSoFar[:], sumSofar, result)
        self.doPathSum(parent.right, target, numsSoFar[:], sumSofar, result)
