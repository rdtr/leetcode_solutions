func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	l1len, l2len := getLen(l1), getLen(l2)
	if l2len > l1len { // make sure l1 is longer
		l1, l2 = l2, l1
		l1len, l2len = l2len, l1len
	}

	// padding l2 (shorter list)
	dummy := &ListNode{}
	cur := dummy
	for i := 0; i < l1len-l2len; i++ {
		cur.Next = &ListNode{Val: 0}
		cur = cur.Next
	}
	cur.Next = l2
	l2 = dummy.Next

	return add(l1, l2)
}

// add adds two list nodes, l1 and l2.
func add(l1 *ListNode, l2 *ListNode) *ListNode {
	if co := doAdd(l1, l2); co == 1 {
		head := &ListNode{Val: 1, Next: l1}
		return head
	}
	return l1
}

// doAdd add two list nodes and return carry over (1 or 0).
func doAdd(l1 *ListNode, l2 *ListNode) int {
	if l1 == nil || l2 == nil {
		return 0
	}

	co := doAdd(l1.Next, l2.Next)
	sum := co + l1.Val + l2.Val
	if sum >= 10 {
		co = 1
		l1.Val = sum - 10
	} else {
		co = 0
		l1.Val = sum
	}
	return co
}

func getLen(node *ListNode) int {
	length := 0
	for node != nil {
		node = node.Next
		length++
	}
	return length
}