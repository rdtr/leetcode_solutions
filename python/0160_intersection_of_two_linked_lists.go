class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        
        lenA, lenB = 0, 0
        curA, curB = headA, headB
        while curA or curB:
            if curA:
                curA, lenA = curA.next, lenA + 1
            if curB:
                curB, lenB = curB.next, lenB + 1
        
        # ensure A is always longer
        if lenB > lenA:
            headA, headB, lenA, lenB = headB, headA, lenB, lenA
        
        curA, curB, diff = headA, headB, lenA - lenB
        while diff > 0:
            curA, diff = curA.next, diff-1
        
        while curA and curB:
            if curA.val == curB.val:
                return curA
            curA, curB = curA.next, curB.next
        return None