func mergeTrees(t1 *TreeNode, t2 *TreeNode) *TreeNode {
	if t1 == nil && t2 == nil {
		return nil
	} else if t1 == nil {
		return t2
	} else if t2 == nil {
		return t1
	}

	t1.Val = t1.Val + t2.Val
	p1, p2 := t1, t2
	helper(p1, p2)
	return t1
}

func helper(p1, p2 *TreeNode) {
	// handle left
	switch {
	case p1.Left == nil && p2.Left != nil:
		p1.Left = p2.Left
	case p1.Left != nil && p2.Left != nil:
		p1.Left.Val = p1.Left.Val + p2.Left.Val
		helper(p1.Left, p2.Left)
	default:
	}

	// handle right
	switch {
	case p1.Right == nil && p2.Right != nil:
		p1.Right = p2.Right
	case p1.Right != nil && p2.Right != nil:
		p1.Right.Val = p1.Right.Val + p2.Right.Val
		helper(p1.Right, p2.Right)
	default:
	}
}

