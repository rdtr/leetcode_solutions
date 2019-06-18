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


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return []

        while len(lists) > 1:
            i = 0
            newlists = []
            while i + 1 < len(lists):
                l1 = lists[i]
                l2 = lists[i + 1]
                newlists.append(merge(l1, l2))
                i += 2
            if i == len(lists) - 1:
                newlists.append(lists[-1])
            lists = newlists
        return lists[0]


def merge(l1, l2):
    dummy = ListNode(0)
    cur = dummy
    while l1 or l2:
        if l1 and l2:
            if l1.val > l2.val:
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next
        elif l1:
            cur.next = l1
            l1 = None
        else:
            cur.next = l2
            l2 = None
        cur = cur.next
    return dummy.next

