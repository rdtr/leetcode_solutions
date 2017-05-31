func preorderTraversal(root *TreeNode) []int {
	res := []int{}
	if root == nil {
		return res
	}

	cur := root
	for cur != nil {
		if cur.Left == nil {
			res = append(res, cur.Val)
			cur = cur.Right
			continue
		}

		next := cur.Left
		visited := false
		for next.Right != nil {
			if next.Right == cur {
				next.Right = nil
				cur = cur.Right
				visited = true
			}
			next = next.Right
		}

		if !visited {
			next.Right = cur
			res = append(res, cur.Val)
			cur = cur.Left
		}
	}
	return res
}

func preorderTraversal(root *TreeNode) []int {
	res := []int{}
	if root == nil {
		return res
	}

	//visited := make(map[*TreeNode]bool)
	stack := []*TreeNode{}
	cur := root
	for {
		res = append(res, cur.Val)

		if cur.Left != nil {
			if cur.Right != nil {
				stack = append(stack, cur.Right)
			}
			cur = cur.Left
			continue
		}

		if cur.Right != nil {
			cur = cur.Right
			continue
		}

		if len(stack) == 0 {
			break
		}
		cur = stack[len(stack)-1]
		stack = stack[:len(stack)-1]
	}

	return res
}