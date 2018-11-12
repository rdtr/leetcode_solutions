# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq


class MyListNode(ListNode):
    def __init__(self, val, nex):
        self.val = val
        self.next = nex

    def __lt__(self, other):
        return self.val < other.val


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        heap = [MyListNode(l.val, l.next) for l in lists if l is not None]
        heapq.heapify(heap)

        res = ListNode(-1)
        cur = res
        while heap:
            smallest = heapq.heappop(heap)
            if smallest.next is not None:
                heapq.heappush(
                    heap, MyListNode(smallest.next.val, smallest.next.next))
            cur.next = smallest
            cur = cur.next
        cur.next = None
        return res.next