package main

func deleteDuplicates(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}
	dummyHead := head

	for head.Next != nil {
		if head.Val == head.Next.Val {
			head.Next = head.Next.Next
			continue
		}
		head = head.Next
	}
	return dummyHead
}
