func reverseList(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}

	prev, cur := head, head.Next
	head.Next = nil // head should be tail after reversing
	var next *ListNode
	for {
		next = cur.Next
		cur.Next = prev

		if next == nil {
			return cur
		}
		prev = cur
		cur = next
	}
	return nil // never reaches here
}