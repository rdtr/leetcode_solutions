package main

func swapPairs(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}

	node := &ListNode{}
	dummyHead := node
	for {
		if head.Next == nil {
			node.Next = head
			break
		}
		if head.Next.Next == nil {
			first, second := head, head.Next
			node.Next = second
			second.Next = first
			first.Next = nil
			break
		}

		first, second, third := head, head.Next, head.Next.Next
		node.Next = second
		second.Next = first
		node = first
		head = third
	}
	return dummyHead.Next
}
