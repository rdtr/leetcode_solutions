# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        c = dummy
        while l1 or l2:
            if l1 and l2:
                if l1.val > l2.val:
                    c.next = l2
                    l2 = l2.next
                else:
                    c.next = l1
                    l1 = l1.next
            elif l1:
                c.next = l1
                l1 = None
            else:
                c.next = l2
                l2 = None
            c = c.next
        return dummy.next
