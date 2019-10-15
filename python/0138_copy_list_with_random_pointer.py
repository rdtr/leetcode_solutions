"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dummy = Node(-1, None, None)

        cur = head
        newcur = dummy
        nodemap = {}
        while cur:
            newNode = Node(cur.val, None, None)
            newcur.next = newNode
            newcur = newcur.next

            nodemap[cur] = newcur
            cur = cur.next

        cur = head
        newcur = dummy.next
        while cur:
            if cur.random:
                newcur.random = nodemap[cur.random]
            cur = cur.next
            newcur = newcur.next

        return dummy.next
