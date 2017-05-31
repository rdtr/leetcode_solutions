func oddEvenList(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}
	if head.Next == nil {
		return head
	}

	oddHead, evenHead := head, head.Next
	oddCur, evenCur := oddHead, evenHead

	var oddStop, evenStop bool
	for !oddStop || !evenStop {
		if oddCur.Next != nil && oddCur.Next.Next != nil {
			oddCur.Next = oddCur.Next.Next
			oddCur = oddCur.Next
		} else {
			oddStop = true
		}
		if evenCur.Next != nil && evenCur.Next.Next != nil {
			evenCur.Next = evenCur.Next.Next
			evenCur = evenCur.Next
		} else {
			evenStop = true
		}
	}
	oddCur.Next, evenCur.Next = evenHead, nil
	return oddHead
}