package main

func removeNthFromEnd(head *ListNode, n int) *ListNode {
	fast, slow := head, head
	for i := 0; i < n; i++ {
		if fast.Next == nil {
			// assuming all n is valid, so this case
			// the first element to be deleted
			return head.Next
		}
		fast = fast.Next
	}

	for fast.Next != nil {
		fast, slow = fast.Next, slow.Next
	}
	slow.Next = slow.Next.Next
	return head
}
