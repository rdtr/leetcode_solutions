class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        slow, fast = head, head

        while True:
            if not fast or not fast.next:
                break
            fast = fast.next.next
            slow = slow.next
            if not fast:
                return False
            elif fast.val == slow.val:
                return True
        return False


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:        
        visited = set([])
        cur = head
        while cur is not None:
            if cur in visited:
                return True
            visited.add(cur)
            cur = cur.next
        return False