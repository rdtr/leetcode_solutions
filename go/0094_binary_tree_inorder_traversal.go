package main

func inorderTraversal(root *TreeNode) []int {
	var res []int

	cur := root
	for cur != nil {
		if cur.Left == nil {
			res = append(res, cur.Val)
			cur = cur.Right
			continue
		}

		pre := cur.Left
		for pre.Right != nil && pre.Right != cur {
			pre = pre.Right
		}

		if pre.Right == nil {
			pre.Right = cur
			cur = cur.Left
		} else {
			pre.Right = nil
			res = append(res, cur.Val)
			cur = cur.Right
		}
	}
	return res
}

func inorderTraversal(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}

	var res []int
	cur, popped := root, false
	queue := []*TreeNode{}
	for {
		if !popped {
			for cur.Left != nil {
				popped = false
				queue = append(queue, cur)
				cur = cur.Left
			}
		}

		res = append(res, cur.Val)
		if cur.Right != nil {
			cur, popped = cur.Right, false
			continue
		}
		if len(queue) > 0 {
			cur, popped = queue[len(queue)-1], true
			queue = queue[:len(queue)-1]
			continue
		}
		break
	}
	return res
}
