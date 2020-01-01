# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        dummy = head
        oddCur = head
        if not head or not head.next:
            return oddCur
        evenCur = head.next
        evenHead = evenCur

        while True:
            oddUpdate, evenUpdate = False, False

            if oddCur and oddCur.next:
                tmp = oddCur.next
                oddCur.next = oddCur.next.next
                if oddCur.next is not None:
                    oddUpdate = True
                    oddCur = oddCur.next
            if evenCur and evenCur.next:
                evenCur.next = evenCur.next.next
                if evenCur.next is not None:
                    evenUpdate = True
                    evenCur = evenCur.next

            if not oddUpdate and not evenUpdate:
                break

        oddCur.next = evenHead
        return dummy
