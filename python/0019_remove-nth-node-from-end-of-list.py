# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        if not head:
            return None
        
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        
        target = length - n
        i = 0
        prev, cur = None, head
        while i < target:
            prev = cur
            cur = cur.next
            i += 1
        
        if cur == head:
            head = cur.next
        else:
            prev.next = cur.next
        return head