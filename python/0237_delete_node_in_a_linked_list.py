class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while True:
            node.val = node.next.val
            if not node.next.next:
                node.next = None
                break
            node = node.next
