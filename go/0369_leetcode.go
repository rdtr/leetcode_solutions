func plusOne(head *ListNode) *ListNode {
	cur := head
	isHeadNine := cur.Val == 9
	var mark *ListNode

	for cur.Next != nil {
		if cur.Next.Val == 9 {
			if mark == nil {
				mark = cur
			}
		} else {
			mark = nil
		}

		cur = cur.Next
	}

	cur.Val += 1
	if cur.Val <= 9 {
		return head
	}

	cur.Val = 0
	for mark != nil && mark != cur {
		mark.Val += 1
		if mark.Val > 9 {
			mark.Val = 0
		}
		mark = mark.Next
	}

	if isHeadNine {
		return &ListNode{Val: 1, Next: head}
	}
	return head
}