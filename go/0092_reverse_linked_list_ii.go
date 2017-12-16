func reverseBetween(head *ListNode, m int, n int) *ListNode {
	if head == nil || head.Next == nil || m == n {
		return head
	}

	var left, right, start, prev, cur, next *ListNode
	cur = head
	next = cur.Next

	i := 1
	for { // iterate until m
		if i == m {
			break
		}
		i++
		prev = cur
		cur = next
		next = next.Next
	}

	left, start = prev, cur
	for { // reverse m to n
		if i > n {
			break
		}
		i++
		cur.Next = prev
		prev = cur
		cur = next
		if next != nil {
			next = next.Next
		}
	}
	right = cur

	// connect left, right and adjust head
	if left == nil {
		head = prev
	} else {
		left.Next = prev
	}
	start.Next = right
	return head
}