class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        carry = 0
        cur = dummy
        while l1 or l2:
            if l1 and l2:
                sum = carry + l1.val + l2.val
                sum, carry = sum % 10, sum // 10
                cur.next = ListNode(sum)
                cur, l1, l2 = cur.next, l1.next, l2.next
            elif l1:
                sum = carry + l1.val
                sum, carry = sum % 10, sum // 10
                cur.next = ListNode(sum)
                cur, l1 = cur.next, l1.next
            else:
                sum = carry + l2.val
                sum, carry = sum % 10, sum // 10
                cur.next = ListNode(sum)
                cur, l2 = cur.next, l2.next
        if carry == 1:
            cur.next = ListNode(1)
        return dummy.next