class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur is not None:
            while cur.next is not None and cur.val == cur.next.val:
                cur.next = cur.next.next
            cur = cur.next
        return head