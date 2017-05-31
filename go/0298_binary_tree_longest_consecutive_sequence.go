func longestConsecutive(root *TreeNode) int {
	if root == nil {
		return 0
	}

	max := 0
	findPath(root, &max, 1)
	return max
}

func findPath(parent *TreeNode, max *int, cur int) {
	origCur := cur
	if cur > *max {
		*max = cur
	}

	var nextCur int
	if parent.Left != nil {
		if parent.Left.Val-1 == parent.Val {
			nextCur = cur + 1
		} else {
			nextCur = 1
		}
		findPath(parent.Left, max, nextCur)
	}

	cur = origCur
	if parent.Right != nil {
		if parent.Right.Val-1 == parent.Val {
			nextCur = cur + 1
		} else {
			nextCur = 1
		}
		findPath(parent.Right, max, nextCur)
	}
}