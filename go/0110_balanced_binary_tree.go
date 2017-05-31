func isBalanced(root *TreeNode) bool {
	_, ok := check(root)
	return ok
}

func check(parent *TreeNode) (int, bool) {
	if parent == nil {
		return 0, true
	}

	l, ok := check(parent.Left)
	if !ok {
		return 0, false
	}
	r, ok := check(parent.Right)
	if !ok {
		return 0, false
	}

	if diff := abs(l - r); diff > 1 {
		return 0, false
	}
	return max(l, r) + 1, true
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func abs(a int) int {
	if a >= 0 {
		return a
	}
	return -a
}