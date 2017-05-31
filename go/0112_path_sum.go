func hasPathSum(root *TreeNode, sum int) bool {
	res := false
	doHasPathSum(root, 0, sum, &res)
	return res
}

func doHasPathSum(parent *TreeNode, currentSum int, targetSum int, result *bool) {
	if parent == nil {
		return
	}
	currentSum += parent.Val
	if *result || (currentSum == targetSum && parent.Left == nil && parent.Right == nil) {
		*result = true
		return
	}
	doHasPathSum(parent.Left, currentSum, targetSum, result)
	doHasPathSum(parent.Right, currentSum, targetSum, result)
}