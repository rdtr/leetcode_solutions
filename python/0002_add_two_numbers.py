# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        head = res

        co = 0
        while (l1 is not None) or (l2 is not None) or co != 0:
            if l1 is None and co == 0:
                res.next = l2
                break
            if l2 is None and co == 0:
                res.next = l1
                break
            sum = 0

            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            sum += co

            co = sum / 10
            sum = sum % 10

            res.next = ListNode(sum)
            res = res.next
        return head.next