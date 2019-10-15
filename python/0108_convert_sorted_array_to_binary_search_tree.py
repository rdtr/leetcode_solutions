# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        nlen = len(nums)
        if nlen == 0:
            return None

        mid = nlen // 2
        root = TreeNode(nums[mid])

        root.left = self.doSortedArrayToBST(nums, 0, mid - 1)
        root.right = self.doSortedArrayToBST(nums, mid + 1, nlen - 1)
        return root

    def doSortedArrayToBST(self, nums, left, right):
        if left > right:
            return
        elif left == right:
            return TreeNode(nums[left])

        mid = left + (right - left) // 2
        parent = TreeNode(nums[mid])

        parent.left = self.doSortedArrayToBST(nums, left, mid - 1)
        parent.right = self.doSortedArrayToBST(nums, mid + 1, right)
        return parent
