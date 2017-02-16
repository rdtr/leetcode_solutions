package main

func reverseKGroup(head *ListNode, k int) *ListNode {
	if head == nil {
		return nil
	}
	if k <= 1 {
		return head
	}

	dummyHead := &ListNode{}
	dummyHead.Next = head
	tail := dummyHead
	curNode := head
	for {
		var shouldStop bool
		var reversingNodes []*ListNode
		for i := 0; i < k; i++ {
			if curNode == nil {
				shouldStop = true
				break
			}
			reversingNodes = append(reversingNodes, curNode)
			curNode = curNode.Next
		}

		if shouldStop {
			// some nodes are left as they are. So connect the tail to the head of those.
			if len(reversingNodes) > 0 {
				tail.Next = reversingNodes[0]
				break
			}
			// a number of nodes can be divisible by n. the tail should have no Next.
			tail.Next = nil
			break
		}

		// reverse
		for i := k - 1; i >= 1; i-- {
			reversingNodes[i].Next = reversingNodes[i-1]
		}
		// connect the tail to the last nodes being reversed
		tail.Next = reversingNodes[len(reversingNodes)-1]
		tail = reversingNodes[0]
	}
	return dummyHead.Next
}
