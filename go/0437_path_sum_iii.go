func pathSum(root *TreeNode, sum int) int {
	if root == nil {
		return 0
	}

	sumMap := make(map[int]int)
	sumMap[0] = 1
	num := 0
	doPathSum(&num, root, 0, sum, sumMap)
	return num
}

func doPathSum(res *int, node *TreeNode, sumSoFar int, target int, cache map[int]int) {
	if node == nil {
		return
	}

	sumSoFar += node.Val
	if cnt, ok := cache[sumSoFar-target]; ok {
		*res += cnt
	}

	if cnt, ok := cache[sumSoFar]; ok {
		cache[sumSoFar] = cnt + 1
	} else {
		cache[sumSoFar] = 1
	}

	doPathSum(res, node.Left, sumSoFar, target, cache)
	doPathSum(res, node.Right, sumSoFar, target, cache)

	cache[sumSoFar]--
}