package main

// note: there is a simpler way to solve this:
//       https://discuss.leetcode.com/topic/70550/golang-solution-0ms

func isSameTree(p *TreeNode, q *TreeNode) bool {
	result := true
	switch {
	case p == nil && q == nil:
		return true
	case (p != nil && q == nil) || (p == nil && q != nil):
		return false
	default:
		if p.Val != q.Val {
			return false
		}
		backtrack(&result, p, q)
	}
	return result
}

func backtrack(curResult *bool, pNode, qNode *TreeNode) {
	if *curResult != true {
		return
	}
	if pNode.Left == nil && pNode.Right == nil && qNode.Left == nil && qNode.Right == nil {
		return
	}

	if pNode.Left != nil && qNode.Left == nil ||
		pNode.Left == nil && qNode.Left != nil ||
		pNode.Right != nil && qNode.Right == nil ||
		pNode.Right == nil && qNode.Right != nil {
		*curResult = false
		return
	}
	if pNode.Left != nil && qNode.Left != nil {

		if pNode.Left.Val != qNode.Left.Val {
			*curResult = false
			return
		}
		backtrack(curResult, pNode.Left, qNode.Left)
	}
	if pNode.Right != nil && qNode.Right != nil {
		if pNode.Right.Val != qNode.Right.Val {
			*curResult = false
			return
		}
		backtrack(curResult, pNode.Right, qNode.Right)
	}

}

//

func isSameTree(p *TreeNode, q *TreeNode) bool {
	if p == nil && q == nil {
		return true
	} else if (p != nil && q == nil) || (p == nil && q != nil) {
		return false
	}

	if p.Val != q.Val {
		return false
	}

	return isSameTree(p.Left, q.Left) && isSameTree(p.Right, q.Right)
}
