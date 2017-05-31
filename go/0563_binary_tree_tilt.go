func findTilt(root *TreeNode) int {
	res := 0
	getSum(root, &res)
	return res
}

func getSum(node *TreeNode, tilt *int) int {
	if node == nil {
		return 0
	}

	lsum, rsum := getSum(node.Left, tilt), getSum(node.Right, tilt)
	diff := lsum - rsum
	if diff < 0 {
		diff = -diff
	}
	*tilt += diff

	return lsum + rsum + node.Val
}