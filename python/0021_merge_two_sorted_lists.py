# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val > l2.val:
            l1, l2 = l2, l1

        p1, p2 = l1, l2
        head = p1
        while p1.next and p2:
            if p1.next.val <= p2.val:
                p1 = p1.next
                continue

            p1Next, p2Next = p1.next, p2.next
            p1.next, p2.next = p2, p1Next

            p1, p2 = p2, p2Next

        if p2:
            p1.next = p2
        return head

