class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None

        dummy, cur = head, head
        while cur and cur.val == val:
            cur = cur.next
            dummy = cur

        while cur:
            if cur.next and cur.next.val == val:
                cur.next = cur.next.next
                continue
            cur = cur.next
        return dummy