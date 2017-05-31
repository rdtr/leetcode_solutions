import "math"

func maxPathSum(root *TreeNode) int {
	if root == nil {
		return 0
	}

	max := math.MinInt32
	getSum(&max, root)
	return max
}

func getSum(max *int, parent *TreeNode) int {
	leftSum, rightSum := 0, 0
	if parent.Left == nil {
		leftSum = 0
	} else {
		leftSum = maxint(getSum(max, parent.Left), 0)
	}

	if parent.Right == nil {
		rightSum = 0
	} else {
		rightSum = maxint(getSum(max, parent.Right), 0)
	}

	*max = maxint(leftSum+rightSum+parent.Val, *max)
	return parent.Val + maxint(leftSum, rightSum)
}

func maxint(a, b int) int {
	if a > b {
		return a
	}
	return b
}
