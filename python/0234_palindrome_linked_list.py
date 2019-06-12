# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        cur = head
        l = 1
        while cur.next:
            cur = cur.next
            l += 1

        mid = l // 2

        i = 1
        prev = None
        cur = head
        next = cur.next
        while i <= mid:
            cur.next = prev

            prev = cur
            cur = next
            next = next.next
            i += 1

        left = prev
        right = cur if l % 2 == 0 else cur.next
        while left:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

