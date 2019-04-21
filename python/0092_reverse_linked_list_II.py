# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        i = 1
        start = head
        prevStart = None
        while i < m:
            prevStart = start
            start = start.next
            i += 1

        prev = None
        cur = start
        next = cur.next
        while i <= n:
            cur.next = prev
            prev = cur
            cur = next
            if cur:
                next = cur.next
            i += 1

        start.next = cur
        if prevStart:
            prevStart.next = prev
            return head
        return prev





