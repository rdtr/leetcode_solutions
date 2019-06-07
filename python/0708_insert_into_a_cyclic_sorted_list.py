"""
# Definition for a Node.
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next
"""


class Solution:
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """

        if head is None:
            return Node(insertVal, None)

        cur = head
        while True:
            if cur.val <= insertVal and insertVal < cur.next.val:
                cur.next = Node(insertVal, cur.next)
                return head
            elif cur.val > cur.next.val and (insertVal < cur.next.val or cur.val <= insertVal):
                cur.next = Node(insertVal, cur.next)
                return head

            if cur.next == head:
                cur.next = Node(insertVal, cur.next)
                return head
            cur = cur.next