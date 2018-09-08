package main

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	if l1 == nil {
		return l2
	} else if l2 == nil {
		return l1
	}

	head := &ListNode{}
	cur := head
	carry := 0
	for l1 != nil && l2 != nil {
		sum := l1.Val + l2.Val + carry
		if sum > 9 {
			sum -= 10
			carry = 1
		} else {
			carry = 0
		}
		cur.Next = &ListNode{Val: sum}
		l1, l2, cur = l1.Next, l2.Next, cur.Next
	}

	if l1 == nil && l2 == nil {
		if carry > 0 {
			cur.Next = &ListNode{Val: 1}
		}
		return head.Next
	}

	var remaining *ListNode
	if l1 != nil {
		remaining = l1
	} else {
		remaining = l2
	}

	for carry > 0 || remaining != nil {
		if carry == 0 {
			cur.Next = remaining
			return head.Next
		}
		if remaining == nil {
			cur.Next = &ListNode{Val: 1}
			return head.Next
		}

		sum := remaining.Val + carry
		if sum > 9 {
			sum -= 10
			carry = 1
		} else {
			carry = 0
		}
		cur.Next = &ListNode{Val: sum}
		remaining, cur = remaining.Next, cur.Next
	}
	return head.Next
}
