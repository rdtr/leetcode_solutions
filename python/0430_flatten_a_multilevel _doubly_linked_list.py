"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        cur = head
        res = head
        stack = []

        while cur:
            if cur.child:
                if cur.next:
                    tmp = cur.next
                    cur.next = None
                    tmp.prev = None
                    stack.append(tmp)

                cur.next = cur.child
                cur.child.prev = cur

                tmp = cur
                cur = cur.child
                tmp.child = None
                continue

            if not cur.next and stack:
                tmp = stack.pop()
                cur.next = tmp
                tmp.prev = cur
            cur = cur.next

        cur = res
        while cur:
            cur = cur.next
        return res
