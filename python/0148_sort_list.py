class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None or head.next is None:
            return head

        slow, fast = head, head
        while True:
            if fast.next is None or fast.next.next is None:
                secondHead, slow.next = slow.next, None
                break
            fast, slow = fast.next.next, slow.next

        first, second = self.sortList(head), self.sortList(secondHead)
        return self.merge(first, second)

    def merge(self, first, second):
        dummyHead = ListNode(0)
        cur = dummyHead

        while first is not None and second is not None:
            if first.val < second.val:
                node = first
                first = first.next
            else:
                node = second
                second = second.next
            cur.next = node
            cur = cur.next

        if first is not None:
            remain = first
        if second is not None:
            remain = second
        while remain is not None:
            node = remain
            remain = remain.next

            cur.next = node
            cur = cur.next

        return dummyHead.next