package main

func partition(head *ListNode, x int) *ListNode {
	first, second := &ListNode{}, &ListNode{}
	dummyHeadFirst, dummyHeadSecond := first, second

	for head != nil {
		if head.Val < x {
			first.Next = head
			first = first.Next
		} else {
			second.Next = head
			second = second.Next
		}
		head = head.Next
	}
	first.Next, second.Next = nil, nil
	if dummyHeadSecond.Next != nil {
		first.Next = dummyHeadSecond.Next
	}
	return dummyHeadFirst.Next
}
